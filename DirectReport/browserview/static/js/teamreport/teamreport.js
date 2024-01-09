'use strict';

const {useState, useCallback, useEffect} = React;

class TeamReport extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            teamData: [],
            repos: [],
            reportData: {},
            commits: [],
            commentText: '',
            repoSelected: false
        }

        this.handleTeamDataChange = this.handleTeamDataChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this)
        this.openRepoPopover = this.openRepoPopover.bind(this);
        this.getRepoData = this.getRepoData.bind(this);
        this.handleRepoDataChange = this.handleRepoDataChange.bind(this);
        this.setCommits = this.setCommits.bind(this);
        this.toggle = this.toggle.bind(this);
        this.toggleHide = this.toggleHide.bind(this);
        this.setComments = this.setComments.bind(this);
        this.setRepoSelected = this.setRepoSelected.bind(this);
        this.handleReportDataChange = this.handleReportDataChange.bind(this);
    }

    toggle() {
        this.setState({isOpened: !this.state.isOpened});
    }

    toggleHide() {
        this.setState({isHidden: !this.state.isHidden});
    }

    handleTeamDataChange(teamD) {
        this.setState({teamData: teamD});
    }

    handleReportDataChange(reportD) {
        this.setState({reportData: reportD});
    }

    setCommits(commitsData) {
        this.setState({commits: commitsData});
    }

    setComments(commentData) {
        this.setState({commentText: commentData});
    }

    handleRepoDataChange(repoD) {
        this.setState({repos: repoD});
    }

    setRepoSelected(repoSelected) {
        document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
        this.setState({repoSelected: repoSelected});
    }

    handleSubmit() {
        const payload = {"prompt": this.state.commentText}
        axios({
            method: 'post',
            url: '/api/reports/update',
            data: payload,
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        }).then(result => {
            this.handleTeamDataChange(result.data["team"]);
            this.handleReportDataChange(result.data["report"]);
            showAllGraphics(result.data, '#map-container', '#map-container2', '#map-container3');
            this.toggle()
            document.getElementById('popLefPurple').classList.toggle("hidden");
            document.getElementById('padding-content').classList.toggle("hidden");
        }).catch(function (response) {
            console.log(response);
        });
    }

    componentDidMount() {
        this.getRepoData();
    }

    getRepoData() {
        axios({
            method: 'get',
            url: '/api/repos',
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        }).then(result => {
            this.handleRepoDataChange(result.data);
        }).catch(function (response) {
            console.log(response);
        });
    }

    update(repoURL) {
        axios({
            method: 'post',
            url: "/api/repo" + repoURL,
            headers: {'content-type': 'application/json'}
        }).then(result => {
            const results = GetResults(result.data["json_array"]);
            const prompt = results.map((commit) => {
                return commit.name + " " + commit.message + " " + commit.commit_author_date + "\n"
            })
            const news = prompt.reduce((a, b) => a + b, '');
            this.setComments(news);
            this.setCommits(results);
            this.handleSubmit();
            document.getElementById('popLefPurple').classList.toggle("hidden");
        }).catch(error => {
            console.log(error);
        })
    }

    openRepoPopover(repos, state) {
        const element = document.getElementById('h1content');
        Popper.createPopper(element, document.getElementById('popover-repo-left-purple'), {
            resize: true
        });
        document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
        document.getElementById('popover-repo-TitleContent').innerHTML = "Repos" + "(" + this.state.repos.length + ")";
        const content = document.getElementById('popover-repo-Content');
        const list_element = document.createElement("ul")
        this.state.repos.map((repo) => {
            const li = document.createElement("li");
            const repoURL = repo["url_repo"].substring(28, repo['url'].length).replace("/", "?repo_url=")
            li.innerHTML = '<span>' + repo["name"] + '</span>'
            {GetRepoListElement(li, repo)}
            li.onclick = () => {
                this.update(repoURL);
                this.setRepoSelected(true);
            }
            list_element.append(li)
        })
        content.appendChild(list_element);
    };

    render() {

        return (
            <div id>
                <h1 id="h1content" className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-10 mb-10 pt-8 mx-30 px-20">Generate Team Report From Metadata</h1>
                {repoPopoverUI()}
                {spinnerUI()}
                <div id="topRow" className="grid grid-cols-3 gap-10 rounded-3xl mx-20 mt-6">
                    {EditSummaryElem({"repos": this.state.repos, "commits": this.state.commits}, this.state, this.openRepoPopover)}
                    {SummarySection(this.state.reportData)}
                    {TeamSection(this.state.teamData, this.closePopover)}
                </div>
                {this.state.commits.length <= 0 && (
                    <div id="padding-content" className="pb-[340px] h-10">
                    </div>
                )}
                {this.state.teamData.length > 0 && (
                    <GraphicsUI/>
                )}
            </div>
        )
    }
}

