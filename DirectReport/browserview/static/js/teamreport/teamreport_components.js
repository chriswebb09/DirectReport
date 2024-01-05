const { useState, useEffect } = React;

const ShowSummary = ({ report }) => {
    return (
        <p id="show_summary" className="w-97 sm:w-97 overflow-y-auto break-words">
            {report && report.summary &&
                <div className="px-2 mb-1 text-xs text-blue-700">
                    {report.summary}
                </div>
            }
        </p>
    );
};

const ShowHighlights = (report) => {

    return (
        <div className="h-30">
            <ul className="px-2 pt-2 pb-3">
                {report["highlights"] !== undefined ?
                    report["highlights"].map(hightlight =>
                        <li className="mt-1 mb-3">
                            <h3 className="font-bold text-xs mb-1 mt-1 text-blue-700">
                                {hightlight.title}
                            </h3>
                            <p className="w-90 sm:w-90 overflow-y-auto text-xs font-sm break-words tracking-wide text-blue-600">
                                {hightlight.description}
                            </p>
                        </li>
                    ) : null
                }
            </ul>
        </div>
    )
}


const ShowTeamList = (team) => {
    return (
        <div class="items-center pt-1 select-none">
            {team !== undefined ?
                team.map(team_member =>
                    <button class="bg-blue-600 py-1 px-2 pb-1 pt-1 mr-0.5 my-0.5 no-underline rounded-full text-white font-sans border-2 border-gray text-xs btn-primary hover:text-white hover:bg-indigo-700 focus:outline-none active:shadow-none" onClick={(event) => openPopover(event, team_member)}>{team_member.name}
                    </button>
                ) : null
            }
        </div>
    )
}

const openPopover = (e: ChangeEvent<HTMLInputElement>, teammember) => {
    // e.preventDefault();
    let element = e.target;
    while ("BUTTON" !== element.nodeName) {
        element = element.parentNode;
    }
    Popper.createPopper(element, document.getElementById('popover-id-left-purple'), {
        strategy: "fixed",
        resize: true
    });
    document.getElementById('popover-id-left-purple').classList.toggle("hidden");
    document.getElementById('popoverTitleContent').innerHTML = teammember.name
    document.getElementById('popoverContent').innerHTML = teammember.accomplishments;
    document.getElementById('popoverCommits').innerHTML = "Commits: " + teammember.commits;
}

const repoPopoverUI = () => {
    return (
        <div className="hidden bg-blue-950 border-0 mx-10 px-15 block z-50 font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-2xl h-68" id="popover-repo-left-purple" style={{zIndex: 2}}>
            <div>
                <div id="popover-repo-Title" className="bg-blue-950 text-white tracking-wide opacity-75 font-bold p-3 mb-0 border-b border-solid border-blueGray-50 uppercase rounded-t-2xl py-4">
                    <span id="popover-repo-TitleContent" className="mx-5"></span>
                    <button className="mx-5 float-right" onClick={closeRepoPopover}>X</button>
                </div>
                <div id="popover-repo-Content" className="text-white font-semibold tracking-wide px-6 py-2 h-2/3 overflow-y-scroll h-36"></div>
                <div id="profile-repo-Button" className="text-white tracking-wide px-6 py-4"></div>
            </div>
        </div>
    )
}

const spinnerUI = () => {
    return (
        <div className="hidden rounded-2xl col-span-1" id="popLefPurple" style={{zIndex: 100}}>
            <div>
                <div role="status" className="mx-0 min-w-full flex flex-col items-center">
                    <div>
                        <svg aria-hidden="true" className="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                                fill="currentColor"/>
                            <path
                                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                                fill="currentFill"/>
                        </svg>
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            </div>
        </div>
    )
}

const closeRepoPopover = () => {
    document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
}

const closePopover = () => {
    document.getElementById('popover-id-left-purple').classList.toggle("hidden");
}

class GraphDiv extends React.Component {

    render() {
        return (
            <div
                className="grid grid-cols-3 gap-12 mt-5 mx-20 bg-blue-600 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl px-5 py-3">
                <div>
                    <h1 id="title_element"
                        className="self-center text-center text-white text-lg text-center font-bold font-mono mb-1 mt-3 py-2">
                        Number of Pull Requests
                    </h1>
                    <div
                        className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl px-10 ml-10"
                        id="dd">
                        <div className="flex justify-center my-2 px-3" id="data_display_div">
                            <div id="map-container" className="pl-2 pr-2 rounded-3xl"></div>
                        </div>
                    </div>
                </div>

                <div>
                <h1 id="title_element"
                        className="self-center text-center text-white text-lg text-center font-bold font-mono mb-1 mt-3 py-2">
                        Commits Over Times
                    </h1>
                    <div
                        className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl" id="dd">
                        <div className="justify-center my-2 px-3" id="data_display_div-r">
                            <div id="map-container2" className="pl-2 pr-2 rounded-3xl"></div>
                        </div>
                    </div>
                </div>

                <div>
                    <h1 id="title_element"
                        className="self-center text-center text-white text-lg text-center font-bold font-mono mb-1 mt-3 py-2">
                        Broad Areas of Work
                    </h1>
                    <div className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl mr-10" id="dd">
                        <div className="justify-center my-2 px-3" id="data_display_div-rr">
                            <div id="map-container3" className="pl-2 pr-2 rounded-3xl"></div>
                        </div>
                    </div>
                </div>

            </div>
        )
    }
}

const GraphicsUI = () => {
    return (
        <div className="">
            <h3 className="text-xl text-blue-800 font-mono font-semibold mt-10 mb-8 mx-10 px-12">Graphic Data</h3>
            <GraphDiv/>
        </div>
    )
}

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