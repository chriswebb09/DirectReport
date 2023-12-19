'use strict';
const { useState, useCallback, useEffect } = React;



class TeamReport extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            teamData: {},
            commits: []
        }
        this.handleTeamDataChange = this.handleTeamDataChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this)
        this.openRepoPopover = this.openRepoPopover.bind(this);
        this.setCommits = this.setCommits.bind(this);
        this.toggle =  this.toggle.bind(this);
        this.toggleHide = this.toggleHide.bind(this);
    }

    toggle() {
        this.setState({isOpened: !this.state.isOpened});
    }

    toggleHide() {
        this.setState({isHidden: !this.state.isHidden});
    }

    handleTeamDataChange(team) {
        this.setState({teamData: team});
    }

    setCommits(commitsData) {
        this.setState({commits: commitsData});
    }

    update(repoURL) {
        axios({
            method: 'post',
            url: "/repo" + repoURL,
            headers: {'content-type': 'application/json'}
        }).then(result => {

            const results = result.data.map((commit) =>{
                console.log(commit)
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
            console.log(results)
            this.setCommits(results);
        }).catch(error => {
            console.log(error);
        })
    }


    handleSubmit(event) {
        var dataForm = {
            "prompt": this.state.commentText
        };
        const formDataJsonString = JSON.stringify(dataForm);
        fetch("/report", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: formDataJsonString
        }).then(function(res) {
            return res.json();
        }).then(function(data) {
            this.handleTeamDataChange(data);
            this.toggle();
            showGraphics(data, '#map-container');
            showGraphics2(data, '#map-container2');
            showGraphics3(data, '#map-container3');
        }).then(function() {
            console.log('done');
        });
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
            li.classList.add("py-10");
            li.classList.add("px-10");
            li.onclick = () => {
                this.update(repoURL);
            }
            list_element.append(li)
        })
        content.appendChild(list_element);
    };



    render() {
        return (
            <div>
                <h1 id="h1content"
                    className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-10 pb-2 mb-2 pt-8 mx-30 px-20">
                    Generate Team Report From Metadata
                </h1>
                {repoPopoverUI()}
                <div id="topRow" className="grid grid-cols-3 gap-10 rounded-3xl mx-20 mt-6">
                    <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
                        <div className="py-1 bg-blue-500 rounded-3xl px-20 shadow-[1.0px_1.0px_2.0px_1.0px_rgba(0,0,0,0.58)]">
                            <h1 id="title_element" className="self-center text-center text-white text-xl text-center font-semibold font-mono mb-1 mt-3">Enter
                                Github Data
                            </h1>
                            <div className="bg-white px-6 rounded-3xl">
                                {this.state.commits.map((commit) => {
                                    return (
                                        <div>
                                            <p className="text-sm">{commit.message}</p>
                                            <p className="text-sm">{commit.name}</p>
                                            <p className="text-sm">{commit.commit_author_date}</p>
                                        </div>
                                    )
                                })}
                            </div>
                            <div className="self-center mb-4 mt-2">
                                <div className="px-10 mx-0 min-w-full flex flex-col items-center">
                                    {this.props.repos.length > 0 && (
                                        <button className="w-80 sm:w-90 bg-slate-100 hover:bg-blue-400 text-blue-500 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2" onClick={(e) => this.openRepoPopover(this.props.repos, this.state)} type="button">Select</button>
                                    )}
                                    {this.props.repos.length <= 0 && (
                                        <button className="w-80 sm:w-90 bg-slate-100 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:bg-blue-400 text-blue-500 hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2" type="button">
                                            <a href='/authorize/github'>Authorize</a>
                                        </button>
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
                        <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                            <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Summary</h1>
                            <div id="summary" className="px-4 mx-0 mb-3 mt-2">
                                {this.props.isOpened && (
                                    <div id="summary-container" className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] overflow-y-scroll h-100 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3 pt-6">
                                        {ShowSummary(this.props.teamData["report"])}
                                        {ShowHighlights(this.props.teamData["report"])}
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                    <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center">
                        <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-4 mb-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                            <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Team</h1>
                            {PopoverUI(closePopover)}
                            <div id="display_team" className="my-3"></div>
                            {this.props.isOpened && (
                                <div className="content-center py-1 h-90 rounded-3xl mb-4 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] mx-1 px-3">
                                    {ShowTeamList(this.props.teamData["team"], openPopover)}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
                {this.props.isOpened && (
                    <GraphicsUI/>
                )}
            </div>
        )
    }


};

// class TeamReport extends React.Component {
//     const [repos, setRepos] = useState([]);
//     // const [teamData, setTeamData] = useState({})
//     // const [commentText, setCommentText] = useState("")
//     // const [isOpened, setIsOpened] = useState(false)
//     constructor(props) {
//
//         super(props);
//
//         this.state = {
//             teamData: {},
//             commentText: "",
//             isHidden: true,
//             isOpened: false
//         };
//         this.handleTeamDataChange = this.handleTeamDataChange.bind(this);
//         this.handleReposChange = this.handleReposChange.bind(this);
//         this.handleSubmit = this.handleSubmit.bind(this);
//         this.openRepoPopover = this.openRepoPopover.bind(this);
//         this.handleClick = this.handleClick.bind(this);
//         this.toggle = this.toggle.bind(this);
//         this.toggleHide = this.toggleHide.bind(this);
//         // this.authorizeRepo = this.authorizeRepo.bind(this)
//     }
//
//     handleTeamDataChange(team) {
//         this.setState({teamData: team});
//     }
//
//     // handleReposChange(repoData) {
//     //     this.setState({repos: repoData});
//     // }
//
//     // authorizeRepo(repoData) {
//     //      fetch("/authorize/github", {
//     //         method: "GET"
//     //         // headers: {
//     //         //     "Content-Type": "application/json",
//     //         //     "Accept": "application/json"
//     //         // }
//     //     }).then(function(res) {
//     //         return res.json();
//     //     }).then(function(data) {
//     //         console.log(data);
//     //         this.toggle();
//     //         showGraphics(data, '#map-container');
//     //         showGraphics2(data, '#map-container2');
//     //         showGraphics3(data, '#map-container3');
//     //     }).then(function() {
//     //         console.log('done');
//     //     });
//     // }
//
//     handleSubmit(event) {
//         var dataForm = {
//             "prompt": this.state.commentText
//         };
//         const formDataJsonString = JSON.stringify(dataForm);
//         fetch("/report", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//                 "Accept": "application/json"
//             },
//             body: formDataJsonString
//         }).then(function(res) {
//             return res.json();
//         }).then(function(data) {
//             this.handleTeamDataChange(data);
//             this.toggle();
//             showGraphics(data, '#map-container');
//             showGraphics2(data, '#map-container2');
//             showGraphics3(data, '#map-container3');
//         }).then(function() {
//             console.log('done');
//         });
//     }
//
//     handleClick(event) {
//         // // event.preventDefault()
//         // var dataForm = {
//         //     "prompt": JSON.stringify(this.state.teamData)
//         // };
//         // const formDataJsonString = JSON.stringify(dataForm);
//         // fetch("/generate_email", {
//         //     method: "POST",
//         //     headers: {
//         //         "Content-Type": "application/json",
//         //         "Accept": "application/json"
//         //     },
//         //     body: formDataJsonString
//         // }).then(function(res) {
//         //     return res.json();
//         // }).then(function(data) {
//         //     console.log(data);
//         //     // setGeneratedEmail(data["email"]);
//         //     this.toggleHide();
//         // });
//     }
//
//     toggle() {
//         this.setState({isOpened: !this.state.isOpened});
//     }
//
//     toggleHide() {
//         this.setState({isHidden: !this.state.isHidden});
//     }
//
//     openRepoPopover() {
//         const element = document.getElementById('h1content');
//         Popper.createPopper(element, document.getElementById('popover-repo-left-purple'), {
//             strategy: 'fixed'
//         });
//         document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
//         document.getElementById('popover-repo-TitleContent').innerHTML = "Repos" + "(" + this.state.repos.length + ")";
//         // var list = createULString(repos)
//         // var list_element = document.createElement("ul");
//         // list_element.innerHTML = roots;
//         // document.getElementById('popover-repo-Content').appendChild(list_element);
//     }
//
//     render() {
//         return (
//             <div>
//                 <h1 id="h1content"
//                     className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-10 pb-2 mb-2 pt-8 mx-30 px-20">
//                     Generate Team Report From Metadata
//                 </h1>
//                 {repoPopoverUI()}
//                 <div id="topRow" className="grid grid-cols-3 gap-10 rounded-3xl mx-20 mt-6">
//                     <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
//                         <div className="py-1 bg-blue-500 rounded-3xl px-20 shadow-[1.0px_1.0px_2.0px_1.0px_rgba(0,0,0,0.58)]">
//                             <h1 id="title_element" className="self-center text-center text-white text-xl text-center font-semibold font-mono mb-1 mt-3">Enter
//                                 Github Data
//                             </h1>
//                             <div className="self-center mb-4 mt-2">
//                                 <div className="px-10 mx-0 min-w-full flex flex-col items-center">
//                                     {repos.length > 0 && (
//                                         <button className="w-80 sm:w-90 bg-slate-100 hover:bg-blue-400 text-blue-500 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2" onClick={(e) => this.openRepoPopover} type="button">Select</button>
//                                     )}
//                                     {repos.length <= 0 && (
//                                         <button className="w-80 sm:w-90 bg-slate-100 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:bg-blue-400 text-blue-500 hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2" type="button">
//                                             <a href='/authorize/github'>Authorize</a>
//                                         </button>
//                                     )}
//                                 </div>
//                             </div>
//                         </div>
//                     </div>
//                     <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
//                         <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
//                             <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Summary</h1>
//                             <div id="summary" className="px-4 mx-0 mb-3 mt-2">
//                                 {this.state.isOpened && (
//                                     <div id="summary-container" className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] overflow-y-scroll h-100 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3 pt-6">
//                                         {ShowSummary(this.state.teamData["report"])}
//                                         {ShowHighlights(this.state.teamData["report"])}
//                                     </div>
//                                 )}
//                             </div>
//                         </div>
//                     </div>
//                     <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center">
//                         <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-4 mb-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
//                             <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Team</h1>
//                             {PopoverUI(closePopover)}
//                             <div id="display_team" className="my-3"></div>
//                             {this.state.isOpened && (
//                                 <div className="content-center py-1 h-90 rounded-3xl mb-4 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] mx-1 px-3">
//                                     {ShowTeamList(this.state.teamData["team"], openPopover)}
//                                 </div>
//                             )}
//                         </div>
//                     </div>
//                 </div>
//                 {this.state.isOpened && (
//                     <GraphicsUI/>
//                 )}
//             </div>
//         )
//     }
// }
//
// //
// // const TeamReport = ({repos}) => {
// //
// //     const [teamData, setTeamData] = useState({})
// //     const [commentText, setCommentText] = useState("")
// //     const [isOpened, setIsOpened] = useState(false)
// //
// //     function handeRepo(name, url) {
// //         // e.preventDefault()
// //         // var dataForm = {
// //         //     "prompt": commentText
// //         // };
// //         // const formDataJsonString = JSON.stringify(dataForm);
// //         var dataForm = {
// //             "repo_name": name,
// //             "repo_url": url
// //         };
// //         const formDataJsonString = JSON.stringify(dataForm);
// //         fetch("/repo/" + name, {
// //             method: "POST",
// //             headers: {
// //                 "Content-Type": "application/json",
// //                 "Accept": "application/json"
// //             },
// //             body: formDataJsonString
// //         }).then(function(res) {
// //             return res.json();
// //         }).then(function(data) {
// //             setTeamData(data);
// //             toggle();
// //             showGraphics(data, '#map-container');
// //             showGraphics2(data, '#map-container2');
// //             showGraphics3(data, '#map-container3');
// //         }).then(function() {
// //             console.log('done');
// //         });
// //     }
// //     const handleSubmit = e => {
// //         e.preventDefault()
// //         var dataForm = {
// //             "prompt": commentText
// //         };
// //         const formDataJsonString = JSON.stringify(dataForm);
// //         fetch("/report", {
// //             method: "POST",
// //             headers: {
// //                 "Content-Type": "application/json",
// //                 "Accept": "application/json"
// //             },
// //             body: formDataJsonString
// //         }).then(function(res) {
// //             return res.json();
// //         }).then(function(data) {
// //             setTeamData(data);
// //             toggle();
// //             showGraphics(data, '#map-container');
// //             showGraphics2(data, '#map-container2');
// //             showGraphics3(data, '#map-container3');
// //         }).then(function() {
// //             console.log('done');
// //         });
// //     };
// //
// //     const handleClick = e => {
// //         e.preventDefault()
// //         var dataForm = {
// //             "prompt": JSON.stringify(teamData)
// //         };
// //         const formDataJsonString = JSON.stringify(dataForm);
// //         fetch("/generate_email", {
// //             method: "POST",
// //             headers: {
// //                 "Content-Type": "application/json",
// //                 "Accept": "application/json"
// //             },
// //             body: formDataJsonString
// //         }).then(function(res) {
// //             return res.json();
// //         }).then(function(data) {
// //             setGeneratedEmail(data["email"]);
// //             toggleHide();
// //         });
// //     }
// //     function toggle() {
// //         setIsOpened(isOpened => !isOpened);
// //     }
// //
// //     function toggleHide() {
// //         setIsHidden(isHidden => !isHidden);
// //     }
// //
// //     const Button = ({handleClick, name}) => {
// //         console.log(`${name} rendered`)
// //         return <button onClick={handleClick}>{name}</button>
// //     }
// //
// //
// //     const FormDiv = ({repos}) => {
// //         return (
// //             <div className="py-1 bg-blue-500 rounded-3xl px-20 shadow-[1.0px_1.0px_2.0px_1.0px_rgba(0,0,0,0.58)]">
// //                 <h1 id="title_element" className="self-center text-center text-white text-xl text-center font-semibold font-mono mb-1 mt-3">Enter
// //                     Github Data
// //                 </h1>
// //                 <div className="self-center mb-4 mt-2">
// //                     <div className="px-10 mx-0 min-w-full flex flex-col items-center">
// //                         {repos.length > 0 && (
// //                             <button
// //                                 className="w-80 sm:w-90 bg-slate-100 hover:bg-blue-400 text-blue-500 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2"
// //                                 onClick={(e) => openRepoPopover(e, repos)} type="button">Select</button>
// //                         )}
// //                         {repos.length <= 0 && (
// //                             <button id="submit_prompt_btn" className="w-80 sm:w-90 bg-slate-100 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:bg-blue-400 text-blue-500 hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2" type="submit">
// //                                 <a className="btn btn-primary" href="/authorize/github">Authorize Github</a>
// //                             </button>
// //                         )}
// //                     </div>
// //                 </div>
// //             </div>
// //         )
// //     }
// //
// //
// //     const openRepoPopover = (e: ChangeEvent<HTMLInputElement>, repos) => {
// //         const element = document.getElementById('h1content');
// //         Popper.createPopper(element, document.getElementById('popover-repo-left-purple'), {
// //             strategy: 'fixed'
// //         });
// //         document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
// //         document.getElementById('popover-repo-TitleContent').innerHTML = "Repos" + "(" + repos.length + ")";
// //         // var list = createULString(repos)
// //         var list_element = document.createElement("ul");
// //         list_element.innerHTML = roots;
// //         document.getElementById('popover-repo-Content').appendChild(list_element);
// //     }
// //
// //
// //
// //     return (
// //         <div>
// //             <h1 id="h1content"
// //                 className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-10 pb-2 mb-2 pt-8 mx-30 px-20">
// //                 Generate Team Report From Metadata
// //             </h1>
// //             {repoPopoverUI()}
// //             <div id="topRow" className="grid grid-cols-3 gap-10 rounded-3xl mx-20 mt-6">
// //                 <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
// //                     {FormDiv({repos})}
// //                 </div>
// //                 <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
// //                     <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
// //                         <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Summary</h1>
// //                         <div id="summary" className="px-4 mx-0 mb-3 mt-2">
// //                             {isOpened && (
// //                                 <div id="summary-container" className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] overflow-y-scroll h-100 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3 pt-6">
// //                                     {ShowSummary(teamData["report"])}
// //                                     {ShowHighlights(teamData["report"])}
// //                                 </div>
// //                             )}
// //                         </div>
// //                     </div>
// //                 </div>
// //                 <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center">
// //                     <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-4 mb-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
// //                         <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Team</h1>
// //                         {PopoverUI(closePopover)}
// //                         <div id="display_team" className="my-3"></div>
// //                         {isOpened && (
// //                             <div className="content-center py-1 h-90 rounded-3xl mb-4 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] mx-1 px-3">
// //                                 {ShowTeamList(teamData["team"], openPopover)}
// //                             </div>
// //                         )}
// //                     </div>
// //                 </div>
// //             </div>
// //             {isOpened && (
// //                 <GraphicsUI/>
// //             )}
// //         </div>
// //     );
// };