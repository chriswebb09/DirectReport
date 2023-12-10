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
            setTeamData(data);
            toggle();
            showGraphics(data);
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
            console.log(res.json());
            return res.json();
        }).then(function(data) {
            setGeneratedEmail(data["email"]);
            toggleHide();
        });
    }

    const closePopover = () => {
        document.getElementById('popover-id-left-purple').classList.toggle("hidden");
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
            <div className="hidden bg-purple-600 border-0 mr-3 block z-50 font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-lg" id="popover-id-left-purple">
                <div>
                    <div id="popoverTitle" className="bg-purple-600 text-white opacity-75 font-semibold p-3 mb-0 border-b border-solid border-blueGray-100 uppercase rounded-t-lg py-3">
                        <span id="popoverTitleContent"></span>
                        <button className="float-right" onClick={closePopover}>X</button>
                    </div>
                    <div id="popoverContent" className="text-white px-6 py-4">
                    </div>
                    <div id="popoverCommits" className="text-white px-6 pb-4">
                    </div>
                    <div id="profileButton" className="text-white px-6 py-4 border-t border-solid border-blueGray-100">
                        <a className="text-md hover:text-gray-200" href="/team">
                            <button type="button" className="w-full text-purple-600 bg-white hover:bg-gray focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800" onClick={closePopover}>
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
            <div className="shadow-lg py-1 border-4 bg-blue-500 rounded-2xl px-30">
                <form onSubmit={handleSubmit}>
                    <h1 className="self-center text-center text-white text-xl text-center font-semibold mb-1 mt-3">Enter
                        Github Data
                    </h1>
                    <div className="self-center mb-6 mt-2">
                        <div className="py-2 px-10 mx-0 min-w-full flex flex-col items-center">
                            <textarea id="prompt_input" cols="30" rows="13" className="self-center shadow-lg py-2 border-4 border-gray-200 w-90 sm:w-90 text-base tracking-wide text-indigo-700 placeholder-white border rounded-2xl focus:shadow-outline" value={commentText} onChange={e => setCommentText(e.target.value)}>
                            </textarea>
                        </div>
                        <div className="px-10 mx-0 min-w-full flex flex-col items-center">
                            <button id="submit_prompt_btn" className="shadow-md w-80 sm:w-90 bg-white hover:bg-blue-700 text-blue-500 hover:text-white border-4 border-gray hover:border-gray-200 text-lg font-semibold py-2 px-10 rounded-lg mt-5" type="submit">
                                Generate
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        )
    }

    function toggle() {
        setIsOpened(isOpened => !isOpened);
    }

    function toggleHide() {
        setIsHidden(isHidden => !isHidden);
    }

    return (
        <div>
            <h1 class="self-center text-center text-2xl text-blue-800 text-center font-bold mb-3 mt-2 mx-10 px-20">
                Generate Team Report From Metadata
            </h1>
            <div className="grid grid-cols-3 gap-8 mb-2 mx-10">
                <div className="lg:col-span-1 sm:col-span-3 justify-center my-2" id="edit_summary_div">
                    {formUI()}
                </div>
                <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center my-2">
                    <div className="shadow-lg py-2 border-4 bg-blue-500 rounded-2xl px-30">
                        <h1 class="self-center text-center text-xl text-white text-center font-semibold mb-1 mt-2 mx-20 px-20">Summary</h1>
                        <div id="summary" className="px-2 mx-0 mb-2 mt-2">
                            {isOpened && (
                                <div id="summary-container" className="bg-white ml-3 mr-3 overflow-y-scroll h-90 rounded-2xl border-4 border-gray tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 mb-6 px-1 py-4">
                                    <p id="show_summary" class="w-97 sm:w-97 overflow-y-auto break-words">
                                        {teamData["report"] !== undefined ?
                                            <div className="px-2 text-sm tracking-wide text-blue-700">{teamData["report"]["summary"]}</div> : null
                                        }
                                    </p>
                                    <div className="h-80">
                                        <ul className="px-2">
                                            {teamData["report"] && teamData["report"]["highlights"].map(hightlight =>
                                                <li className="mb-3">
                                                    <h3 className="font-bold text-md mb-1 tracking-wide text-blue-700">{hightlight.title}</h3>
                                                    <p class="w-90 sm:w-90 overflow-y-auto text-sm font-sm break-words tracking-wide text-blue-600">{hightlight.description}</p>
                                                </li>
                                            )}
                                        </ul>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
                <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center my-2">
                    <div className="shadow-lg py-1 border-4 bg-blue-500 rounded-2xl px-4 mb-2">
                        <h1 class="self-center text-center text-xl text-white text-center font-semibold mb-1 mt-3 mx-20 px-20">Team</h1>
                        {popoverUI()}
                        <div id="display_team" className="my-3"></div>
                        {isOpened && (
                            <div className="content-center py-2 h-90 rounded-2xl ml-3 mb-4 border-4 bg-slate-100 mx-2 px-2">
                                <div className="items-center my-2 mx-2 px-2 select-none">
                                    {teamData["team"] &&
                                        teamData["team"].map(teammember =>
                                            <button class="bg-blue-600 py-1 px-3 pb-2 pt-2.5 mr-2 my-2 shadow-md no-underline rounded-full text-white font-sans border-2 border-gray font-medium text-sm btn-primary hover:text-white hover:bg-indigo-700 focus:outline-none active:shadow-none" onClick={((e) => openPopover(e, teammember))}>{teammember.name}</button>
                                        )}
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
            {isOpened && (
                <div className="grid grid-cols-3 gap-10 mt-5 mb-5 mx-10 border-4 border-indigo-700 shadow-lg rounded-2xl px-30">
                    <div className="lg:col-span-1 sm:col-span-3 justify-center my-10 border-4 border-indigo-700 rounded-2xl px-30 ml-10" id="dd">
                        <div className="col-span-1 justify-center my-10 px-5" id="data_display_div">
                            <div className="border-4 rounded-2xl px-2 mx-5 mb-8 mt-8">
                                <div id="map-container" className="py-5"></div>
                            </div>
                        </div>
                    </div>
                    <div className="lg:col-span-1 sm:col-span-3 justify-center my-10  border-4 border-indigo-700 rounded-2xl px-30 mx-5" id="dd">
                        <div className="col-span-1 justify-center my-10 px-5" id="data_display_div-r">
                            <div id="new" className="border-4 rounded-2xl px-30 px-2 mx-0 mb-8 mt-8">
                                <div id="map-con" className="py-5"></div>
                            </div>
                        </div>
                    </div>
                    <div className="lg:col-span-1 sm:col-span-3 justify-center my-10  border-4 border-indigo-700 rounded-2xl px-30 mr-10" id="dd">
                        <div className="col-span-1 justify-center my-10 px-5" id="data_display_div-rr">
                            <div id="newr" className="border-4 rounded-2xl px-30 px-2 mx-0 mb-8 mt-8">
                                <div id="map-corn" className="py-5"></div>
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
