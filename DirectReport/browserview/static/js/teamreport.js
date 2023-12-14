const { useState, useEffect } = React;
const TeamData = () => {
    const [teamData, setTeamData] = useState({});
    const [commentText, setCommentText] = useState("")
    const [generatedEmail, setGeneratedEmail] = useState("")
    const [isOpened, setIsOpened] = useState(false);
    const [isHidden, setIsHidden] = useState(false);
    const handleSubmit = e => {
        e.preventDefault()
        var dataForm = {
            "prompt": commentText
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
            console.log(data);
            setTeamData(data);
            toggle();
            showGraphics(data, '#map-container');
            showGraphics2(data, '#map-container2');
            showGraphics3(data, '#map-container3');
        }).then(function() {
            console.log('done');

        });
    };

    const handleClick = e => {

        e.preventDefault()

        var dataForm = {
            "prompt": JSON.stringify(teamData)
        };
        const formDataJsonString = JSON.stringify(dataForm);
        fetch("/generate_email", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: formDataJsonString
        }).then(function(res) {
            return res.json();
        }).then(function(data) {
            setGeneratedEmail(data["email"]);
            toggleHide();
        });
    }

    const closePopover = () => {
        document.getElementById('popover-id-left-purple').classList.toggle("hidden");
    }

     const closeRepoPopover = () => {
        document.getElementById('popover-repos').classList.toggle("hidden");
    }


    const openPopover = (e: ChangeEvent<HTMLInputElement>, teammember) => {
        e.preventDefault();
        let element = e.target;
        while("BUTTON" !== element.nodeName) {
            element = element.parentNode;
        }
        Popper.createPopper(element, document.getElementById('popover-id-left-purple'), {
            strategy: 'fixed'
        });
        document.getElementById('popover-id-left-purple').classList.toggle("hidden");
        const popoverTitle = document.getElementById('popoverTitleContent');
        popoverTitle.innerHTML = teammember.name
        const popoverContent = document.getElementById('popoverContent');
        popoverContent.innerHTML = teammember.accomplishments;
        const popoverCommits = document.getElementById('popoverCommits');
        popoverCommits.innerHTML = "Commits: " + teammember.commits;
    }

    const popoverUI = () => {
        return (
            <div className="hidden bg-indigo-600 border-0 mr-3 block z-50 font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-lg" id="popover-id-left-purple">
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

    const formUI = () => {
        return (
            <div className="py-1 bg-blue-500 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.48)]">
                <form onSubmit={handleSubmit}>
                    <h1 className="self-center text-center text-white text-xl text-center font-semibold font-mono mb-1 mt-3">Enter
                        Github Data
                    </h1>
                    <div className="self-center mb-4 mt-2">
                        <div className="py-2 px-10 mx-0 min-w-full flex flex-col items-center">
                            <textarea id="prompt_input" cols="34" rows="11"
                                      className="self-center py-2 border-2 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.28)] border-gray-200 w-90 h-78 sm:w-90 text-base tracking-wide text-indigo-700 placeholder-white border rounded-3xl focus:shadow-outline"
                                      value={commentText} onChange={e => setCommentText(e.target.value)}>
                            </textarea>
                        </div>
                        <div className="px-10 mx-0 min-w-full flex flex-col items-center">
                            <button id="submit_prompt_btn"
                                    className="w-80 sm:w-90 bg-slate-100 hover:bg-blue-400 text-blue-500 hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2"
                                    type="submit">
                                Generate
                            </button>
                            <p></p>
                            <button
                                className="w-80 sm:w-90 bg-slate-100 hover:bg-blue-400 text-blue-500 hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2"
                                onClick={(e) => openRepoPopover(e)} type="button">Repos</button>
                        </div>
                    </div>
                </form>
            </div>
        )
    }

    const openRepoPopover = (e: ChangeEvent<HTMLInputElement>) => {
        const element = document.getElementById('formUI');
        Popper.createPopper(element, document.getElementById('popover-repo-left-purple'), {
            strategy: 'fixed',
            modifiers: [
                {
                    name: "offset", //offsets popper from the reference/button
                    options: {
                        offset: [0, 8]
                    }

                },
                {
                    name: "flip", //flips popper with allowed placements
                    options: {
                        allowedAutoPlacements: ["right", "left", "top", "bottom"],
                        rootBoundary: "viewport"
                    }
                }
            ]
        });
        document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
        const popoverReposTitleContent = document.getElementById('popover-repo-TitleContent');
        popoverReposTitleContent.innerHTML = "Repos" + "(" + teamData["repos"].length + ")";
        const popoverRepoContent = document.getElementById('popover-repo-Content');
        var myList = '<ul className="px-30 py-30">';
        for (var i = 0; i < teamData["repos"].length; i++) {
            myList += '<li>' + '<a href=/repo/' + teamData["repos"][i] + '>' + teamData["repos"][i] + '' + '</li>';
        }
        myList += '</ul>';
        console.log(myList)
        popoverRepoContent.innerHTML = myList;
    }

    const repoPopoverUI = () => {
        return (
            <div
                className="hidden bg-indigo-600 border-0 mr-3 block z-50 font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-lg"
                id="popover-repo-left-purple" style={{zIndex: -1}}>
                <div>
                    <div id="popover-repo-Title"
                         className="bg-indigo-600 text-white opacity-75 font-semibold p-3 mb-0 border-b border-solid border-blueGray-100 uppercase rounded-t-lg py-3">
                        <span id="popover-repo-TitleContent">
                        </span>
                        <button className="float-right" onClick={closeRepoPopover}>
                            X
                        </button>
                    </div>
                    <div id="popover-repo-Content" className="text-white px-6 py-4">
                    </div>
                    {/*<div id="profile-repo-Button" className="text-white px-6 py-4 border-t border-solid border-blueGray-100">*/}

                    {/*</div>*/}
                </div>
            </div>
        )
    }

    function toggle() {
        setIsOpened(isOpened => !isOpened);
    }

    function toggleHide() {
        setIsHidden(isHidden => !isHidden);
    }

    function toggle() {
        setIsOpened(isOpened => !isOpened);
    }

    return (
        <div>
            <h1 className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-3 pb-2 mb-2 pt-4 mx-10 px-20">
                Generate Team Report From Metadata
            </h1>
            {repoPopoverUI()}
            <div id="topRow" className="grid grid-cols-3 gap-8 rounded-3xl mx-10 mt-6">

                <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
                    {formUI()}
                </div>
                <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
                    <div
                        className="pb-6 pt-2 bg-blue-500 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.48)]">
                        <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">
                            Summary
                        </h1>
                        <div id="summary" className="px-4 mx-0 mb-3 mt-2">
                            {isOpened && (
                                <div id="summary-container"
                                     className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.28)] overflow-y-scroll h-100 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3 pt-6 pb-20">
                                    <p id="show_summary" class="w-97 sm:w-97 overflow-y-auto break-words">
                                        {teamData["report"] !== undefined ?
                                            <div className="px-2 mb-1 text-xs text-blue-700">
                                                {teamData["report"]["summary"]}
                                            </div> : null
                                        }
                                    </p>
                                    <div className="h-40">
                                        <ul className="px-2 pt-2 pb-2">
                                            {teamData["report"]["highlights"] && teamData["report"]["highlights"].map(hightlight =>
                                                <li className="mt-1 mb-3">
                                                    <h3 className="font-bold text-sm mb-1 mt-1 text-blue-700">
                                                        {hightlight.title}
                                                    </h3>
                                                    <p class="w-90 sm:w-90 overflow-y-auto text-xs font-sm break-words tracking-wide text-blue-600">
                                                        {hightlight.description}
                                                    </p>
                                                </li>
                                            )}
                                        </ul>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
                <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center">
                    <div
                        className="pb-6 pt-2 bg-blue-500 rounded-3xl px-4 mb-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.48)]">
                        <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Team</h1>
                        {popoverUI()}
                        <div id="display_team" className="my-3"></div>
                        {isOpened && (
                            <div
                                className="content-center py-1 h-90 rounded-3xl mb-4 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.28)] mx-1 px-3">
                                <div className="items-center my-1 select-none">
                                    {teamData["team"] &&
                                        teamData["team"].map(teammember =>
                                            <button
                                                class="bg-blue-600 py-1 px-2 pb-1 pt-1 mr-0.5 my-0.5 no-underline rounded-full text-white font-sans border-2 border-gray text-xs btn-primary hover:text-white hover:bg-indigo-700 focus:outline-none active:shadow-none"
                                                onClick={((e) => openPopover(e, teammember))}>{teammember.name}</button>
                                        )}
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>

            {isOpened && (
                <div>
                    <h3 className="text-xl text-blue-800 text-left font-mono font-semibold mt-10 mb-5 mx-5 px-12">
                        Data
                    </h3>
                    <div
                        className="grid grid-cols-3 gap-6 mt-5 mx-10 bg-blue-500 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.48)] rounded-3xl px-30 py-3">
                        <div
                            className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.28)] rounded-3xl px-30 ml-10"
                            id="dd">
                            <div className="col-span-1 flex justify-center my-2 px-3" id="data_display_div">
                                <div id="map-container" className="pl-10 pr-5">
                                </div>
                            </div>
                        </div>
                        <div
                            className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.28)] rounded-3xl px-30 mx-6"
                            id="dd">
                            <div className="col-span-1 justify-center my-2 px-3" id="data_display_div-r">
                                <div id="map-container2" className="pl-5 pr-5">
                                </div>
                            </div>
                        </div>
                        <div
                            className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.28)] rounded-3xl px-30 mr-10"
                            id="dd">
                            <div className="col-span-1 justify-center my-2 px-3" id="data_display_div-rr">
                                <div id="map-container3" className="pl-5 pr-10">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

const domContainer = document.querySelector('#root');
ReactDOM.render(<TeamData/>, domContainer);
