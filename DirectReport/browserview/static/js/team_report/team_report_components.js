const { useState, useEffect, memo } = React;

// Define a functional component named 'ShowSummary'
const ShowSummary = memo(function ShowSum({report}) {
    return (
        <p id="show_summary" className="w-97 sm:w-97 overflow-y-auto break-words">
            {report && report.summary &&
                <div className="px-2 mb-1 text-xs text-blue-700">
                    {report.summary}
                </div>
            }
        </p>
    );
})


// Define a functional component named 'ShowHighlights'
const ShowHighlights = memo(function ShowHigh({report}) {
    return (
        <div className="h-30">
            <ul className="px-2 pt-2 pb-3">
                {/* Check if 'highlights' in report is not undefined */}
                {report["highlights"] !== undefined ?
                    // Map each highlight to an HTML structure
                    report["highlights"].map(hightlight =>
                        <li className="mt-1 mb-3">
                            <h3 className="font-bold text-xs mb-1 mt-1 text-blue-700">
                                {hightlight.title}
                            </h3>
                            <p className="w-90 sm:w-90 overflow-y-auto text-xs font-sm break-words tracking-wide text-blue-600">
                                {hightlight.description}
                            </p>
                        </li>
                    ) : null // Render nothing if 'highlights' is undefined
                }
            </ul>
        </div>
    )
})


const ShowTeamList = (team) => {
    return (
        <div class="items-center pt-1 select-none">
            {team !== undefined && team.length > 0?
                team.map(team_member =>
                    <button class="bg-blue-600 py-1 px-2 pb-1 pt-1 mr-0.5 my-0.5 no-underline rounded-full text-white font-sans border-2 border-gray text-xs btn-primary hover:text-white hover:bg-indigo-700 focus:outline-none active:shadow-none" onClick={(event) => openPopover(event, team_member)}>
                        {team_member.name}
                    </button>
                ) : null
            }
        </div>
    )
}

const openPopover = (e: ChangeEvent<HTMLInputElement>, team_member) => {
    let element = e.target;
    while ("BUTTON" !== element.nodeName) {
        element = element.parentNode;
    }
    Popper.createPopper(element, document.getElementById('popover-id-left-purple'), {
        strategy: "fixed",
        resize: true
    });
    document.getElementById('popover-id-left-purple').classList.toggle("hidden");
    document.getElementById('popoverTitleContent').innerHTML = team_member.name
    let a = document.createElement('a');
    a.setAttribute('href',"https://www.github.com/" + team_member.github_username);
    a.innerHTML = "Github Profile"
    let p = document.createElement("p");
    p.innerHTML = team_member.accomplishments + "<br/> <br/>";
    p.appendChild(a);
    document.getElementById('popoverContent').appendChild(p);
    document.getElementById('popoverCommits').innerHTML = "Commits: " + team_member.commits;
}

const RepoPopoverUI = () => {
    return (
        <div className="hidden bg-blue-950 border-0 mx-10 px-35 block font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-2xl h-68" id="popover-repo-left-purple" style={{zIndex: 2}}>
            <div>
                <div id="popover-repo-Title" className="bg-blue-950 text-white tracking-wide opacity-75 font-bold p-3 mb-0 border-b border-solid border-blueGray-50 uppercase rounded-t-2xl py-4">
                    <span id="popover-repo-TitleContent" className="px-5 mx-25"></span>
                    <button className="mx-5 float-right" onClick={closeRepoPopover}>X</button>
                </div>
                <div id="popover-repo-Content" className="text-white font-semibold tracking-wide px-6 h-2/3 overflow-y-scroll h-36"></div>
                <div id="profile-repo-Button" className="text-white tracking-wide px-6 py-4"></div>
            </div>
        </div>
    )
}

const SummarySection = (props) => {
    let reportData = props["reportData"];
    return (
        <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
            <div className="pb-6 pt-2 bg-blue-600 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                <h1 className="self-center text-center text-xl text-white text-center font-bold font-mono mb-1 mt-3 py-2 mt-2 mx-20 px-20">Summary</h1>
                <div id="summary" className="px-4 mx-0 mb-1 mt-1">
                    {reportData && reportData["highlights"] !== undefined && (
                        <div id="summary-container" className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] overflow-y-scroll h-100 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3">
                            <div>
                                <ShowSummary report={reportData}/>
                                <ShowHighlights report={reportData}/>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}

const TeamSection = (props) => {
    let propData = props.props;
    let teamData = propData["teamData"];
    return (
        <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center">
            <div className="pb-6 pt-2 bg-blue-600 rounded-3xl px-4 mb-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                <h1 className="self-center text-center text-xl text-white text-center font-bold font-mono mb-1 mt-3 py-2 mx-20 px-20">Team</h1>
                {PopoverUI(closePopover)}
                {teamData && teamData.length > 0 && (
                    <div className="content-center py-2 h-90 rounded-3xl mb-1 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] mx-1 mt-3 px-3">
                        {ShowTeamList(teamData)}
                    </div>
                )}
            </div>
        </div>
    )
}


const GithubEntry = (commit) => {
    return (
        <div className="h-30 mb-4 mt-2">
            <p className="text-xs font-sm break-words tracking-wide text-blue-600">{commit.message}</p>
            <p className="text-xs font-sm break-words tracking-wide text-blue-600">{commit.name}</p>
            <p className="text-xs font-sm break-words tracking-wide text-blue-600">{commit.commit_author_date}</p>
        </div>
    )
}

const GithubButtonElement = (props) => {
    let repos = props["repos"];
    let openRepoPopover = props["openRepoPopover"];
    let state = props["state"];
    return (
        <div className="self-center mb-1 mt-1">
            <div className="mx-0 min-w-full flex flex-col items-center">
                {repos && (
                    <button className="bg-white hover:bg-slate-100 self-center text-blue-600 font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-md font-bold py-3 px-12 rounded-3xl mt-2 mb-3" onClick={(e) => openRepoPopover({repos}, {state})} type="button">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-7 w-6 inline-block ml-10" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                        </svg>
                        <span className="px-4 py-2 tracking-wide">
                            {state.repoSelected ? 'Generate Report' : 'Repository'}
                        </span>
                    </button>
                )}
            </div>
        </div>
    )
}

const GithubEntryElement = (commits) => {
    return (
        <div>
            {commits && (
                <div className="bg-white px-6 rounded-3xl h-80 overflow-y-auto mb-4 mt-4 pt-2">
                    {commits.map((commit) => {
                        return (
                            <div>
                                {GithubEntry(commit)}
                            </div>
                        )
                    })}
                </div>
            )}
        </div>
    )
}

const GetResults = (result) => {
    const results = result.map((commit) => {
        return {
            'message': commit["commit"].message,
            'name': commit["author"]["name"],
            'author_url': commit["author"]["html_url"],
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
    return results
}

const GetRepoListElement = (li) => {
    li.classList.add("py-5");
    li.classList.add("px-3");
    li.classList.add("border-b");
    li.classList.add("border-solid");
    li.classList.add("border-blueGray-100");
}

const EditSummaryElem = memo(function EdSummaryElem({props}) {
    let commits = props['commits'];
    return (
        <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
            <div className="pb-6 pt-2 bg-blue-600 rounded-3xl px-6 shadow-[1.0px_1.0px_2.0px_1.0px_rgba(0,0,0,0.58)]">
                <h1 id="title_element" className="self-center text-center text-white text-xl text-center font-bold font-mono mb-1 mt-3 py-2">
                    Github Data
                </h1>
                {commits && commits.length > 0 && (
                    GithubEntryElement(commits)
                )}
                {GithubButtonElement(props)}
            </div>
        </div>
    )
})

const PopoverUI = (closePopover) => {
    return (
        <div
            className="hidden bg-indigo-600 border-0 mr-3 block z-50 font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-lg" id="popover-id-left-purple">
            <div>
                <div id="popoverTitle" className="bg-indigo-600 text-white opacity-75 font-semibold p-3 mb-0 border-b border-solid border-blueGray-100 uppercase rounded-t-lg py-3">
                        <span id="popoverTitleContent">
                        </span>
                    <button className="float-right" onClick={closePopover}>
                        X
                    </button>
                </div>
                <div id="popoverContent" className="text-white px-6 py-4">
                </div>
                <div id="popoverCommits" className="text-white px-6 pb-4">
                </div>
                <div id="profileButton" className="text-white px-6 py-4 border-t border-solid border-blueGray-100">
                    <a className="text-md hover:text-gray-200" href="/team">
                        <button type="button" className="w-full text-indigo-600 bg-white hover:bg-gray focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" onClick={closePopover}>
                            Profile
                        </button>
                    </a>
                </div>
            </div>
        </div>
    )
}