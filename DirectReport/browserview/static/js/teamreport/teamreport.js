'use strict';

const { useState, useCallback, useEffect } = React;

class TeamReport extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            teamData: [],
            repos: [],
            reportData: {},
            commits: [],
            commentText: ''
        }

        this.handleTeamDataChange = this.handleTeamDataChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this)
        this.openRepoPopover = this.openRepoPopover.bind(this);
        this.getRepoData = this.getRepoData.bind(this);
        this.handleRepoDataChange = this.handleRepoDataChange.bind(this);
        this.setCommits = this.setCommits.bind(this);
        this.toggle =  this.toggle.bind(this);
        this.toggleHide = this.toggleHide.bind(this);
        this.setComments = this.setComments.bind(this);
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

    handleSubmit() {
        const payload = {"prompt": this.state.commentText};
        console.log(payload);
        axios({
            method: 'post',
            url: '/dashboard/reports/update',
            data: payload,
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        }).then(result => {
            console.log(result.data);
            this.handleTeamDataChange(result.data["team"]);
            this.handleReportDataChange(result.data["report"]);
            showGraphics(result.data, '#map-container');
            showGraphics2(result.data, '#map-container2');
            showGraphics3(result.data, '#map-container3');
            this.toggle()
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
            url: '/repos',
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        }).then(result => {
            console.log(result.data);
            this.handleRepoDataChange(result.data);
            // console.log(result.data);
            // this.handleTeamDataChange(result.data["team"]);
            // this.handleReportDataChange(result.data["report"]);
            // showGraphics(result.data, '#map-container');
            // showGraphics2(result.data, '#map-container2');
            // showGraphics3(result.data, '#map-container3');
        }).catch(function (response) {
            console.log(response);
        });
    }

    update(repoURL) {
        axios({
            method: 'post',
            url: "/repo" + repoURL,
            headers: {'content-type': 'application/json'}
        }).then(result => {
            this.setComments(result.data['result_log'])

            const results = result.data['json_array'].map((commit) => {
                return {
                    'message': commit['commit']['message'],
                    'name': commit['commit']['author']['name'],
                    'authur_url': commit['author']['html_url'],
                    'author_name': commit['author']['login'],
                    'commit_author_email': commit['commit']['author']['email'],
                    'commit_author_name': commit['commit']['author']['name'],
                    'commit_author_date': commit['commit']['author']['date'],
                    'committer': commit['commit']['committer']['name'],
                    'committer_data': commit['commit']['committer']['date'],
                    'committer_email': commit['commit']['committer']['email'],
                    'comment_count': commit['commit']['comment_count'],
                    'type': 'commit'
                }
            })
            this.setCommits(results);
            console.log(results)
            this.handleSubmit();
        }).catch(error => {
            console.log(error);
        })
    }

    openRepoPopover(repos, state) {
        const element = document.getElementById('h1content');
        Popper.createPopper(element, document.getElementById('popover-repo-left-purple'), {
            strategy: 'fixed'
        });
        document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
        document.getElementById('popover-repo-TitleContent').innerHTML = "Repos" + "(" + repos.length + ")";
        const content = document.getElementById('popover-repo-Content');
        var list_element = document.createElement("ul")
        repos.map((repo) => {
            var li = document.createElement("li");
            var repoURL = repo["url_repo"].substring(28, repo['url'].length).replace("/", "?repo_url=")
            li.innerHTML = '<span>' + repo["name"] + '</span>'
            li.classList.add("py-5");
            li.classList.add("px-3");
            li.classList.add("border-b");
            li.classList.add("border-solid");
            li.classList.add("border-blueGray-100");
            li.onclick = () => {
                this.update(repoURL);
                document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
            }
            list_element.append(li)
        })
        content.appendChild(list_element);
    };

    render() {
        return (
            <div>
                <h1 id="h1content" className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-10 pb-2 mb-8 pt-8 mx-30 px-20">
                    Generate Team Report From Metadata
                </h1>
                {repoPopoverUI()}
                <div id="topRow" className="grid grid-cols-3 gap-10 rounded-3xl mx-20 mt-6">
                    <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
                        <div className="py-1 bg-blue-500 rounded-3xl px-6 shadow-[1.0px_1.0px_2.0px_1.0px_rgba(0,0,0,0.58)]">
                            {this.state.repos.length > 0 && (
                                <h1 id="title_element" className="self-center text-center text-white text-xl text-center font-bold font-mono mb-1 mt-3 py-2">
                                    Github Repo For Report
                                </h1>
                            )}
                            {this.state.repos.length <= 0 && (
                                <h1 id="title_element" className="self-center text-center text-white text-xl text-center font-bold font-mono mb-1 mt-3 py-2">
                                    Github Account
                                </h1>
                            )}
                            {this.state.commits.length > 0 && (
                                <div className="bg-white px-6 rounded-3xl h-80 overflow-y-auto mb-4 mt-4 pt-2">
                                    {this.state.commits.map((commit) => {
                                        return (
                                            <div className="h-30 mb-4 mt-2">
                                                <p className="text-xs font-sm break-words tracking-wide text-blue-600">{commit.message}</p>
                                                <p className="text-xs font-sm break-words tracking-wide text-blue-600">{commit.name}</p>
                                                <p className="text-xs font-sm break-words tracking-wide text-blue-600">{commit.commit_author_date}</p>
                                            </div>
                                        )
                                    })}
                                </div>
                            )}
                            <div className="self-center mb-4 mt-2">
                                <div className="mx-0 min-w-full flex flex-col items-center">
                                    {this.state.repos.length > 0 && (
                                        <button className="bg-cyan-400 hover:bg-slate-100 self-center text-white font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-md font-bold py-3 px-10 rounded-3xl mt-2 mb-3"
                                                onClick={(e) => this.openRepoPopover(this.state.repos, this.state)}
                                                type="button">
                                            <span className="px-10 py-2 tracking-wide">Select Repo</span>
                                        </button>
                                    )}
                                    {this.state.repos.length <= 0 && (
                                        <button className="bg-cyan-400 hover:bg-slate-100 self-center text-white font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-md font-bold py-3 px-5 rounded-3xl mt-2 mb-3" type="button" onClick={this.getRepoData}>
                                            {/*<a className="px-20 py-2 tracking-wide" href='/repos'>Select Repo</a>*/}
                                            Select Repo
                                        </button>
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
                        <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                            <h1 className="self-center text-center text-xl text-white text-center font-bold font-mono mb-1 mt-3 py-2 mt-2 mx-20 px-20">Summary</h1>
                            <div id="summary" className="px-4 mx-0 mb-1 mt-1">
                                {this.state.teamData.length > 0 && (
                                    <div id="summary-container"
                                         className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] overflow-y-scroll h-100 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3">
                                        {ShowSummary(this.state.reportData)}
                                        {ShowHighlights(this.state.reportData)}
                                    </div>
                                )}

                            </div>
                        </div>
                    </div>
                    <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center">
                        <div
                            className="pb-6 pt-2 bg-blue-500 rounded-3xl px-4 mb-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                            <h1 className="self-center text-center text-xl text-white text-center font-bold font-mono mb-1 mt-3 py-2 mx-20 px-20">Team</h1>
                            {PopoverUI(closePopover)}
                            {this.state.teamData.length > 0 && (
                                <div className="content-center py-2 h-90 rounded-3xl mb-1 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] mx-1 mt-3 px-3">
                                    {ShowTeamList(this.state.teamData)}
                                </div>

                            )}

                        </div>
                    </div>
                </div>
                 {this.state.teamData.length <= 0 && (
                    <div className="pb-50 pt-40 mt-30 h-30">
                    </div>
                )}
                {this.state.teamData.length > 0 && (
                    <GraphicsUI/>
                )}

            </div>
        )
    }
};

