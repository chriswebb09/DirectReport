const { useState, useEffect } = React;

const TeamReport = () => {

    const [teamData, setTeamData] = useState({})
    const [commentText, setCommentText] = useState("")
    const [isOpened, setIsOpened] = useState(false)

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
        document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
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
        document.getElementById('popoverTitleContent').innerHTML = teammember.name
        document.getElementById('popoverContent').innerHTML = teammember.accomplishments;
        document.getElementById('popoverCommits').innerHTML = "Commits: " + teammember.commits;
    }

     const openRepoPopover = (e: ChangeEvent<HTMLInputElement>) => {
        const element = document.getElementById('h1content');
        Popper.createPopper(element, document.getElementById('popover-repo-left-purple'), {
           strategy: 'fixed'
        });
        document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
        document.getElementById('popover-repo-TitleContent').innerHTML = "Repos" + "(" + teamData["repos"].length + ")";
        var list = '<ul>';
        for (var i = 0; i < teamData["repos"].length; i++) {
            list += '<li class="px-1 py-2 border-b border-solid border-blueGray-100 hover:bg-gray-400">' + '<a className="px-8 py-10" href=/repo/' + teamData["repos"][i] + '>' + teamData["repos"][i] + '' + '</li>';
        }
        list += '</ul>';
        document.getElementById('popover-repo-Content').innerHTML = list;
    }

    const repoPopoverUI = () => {
        return (
            <div className="hidden bg-indigo-600 border-0 mx-3 block z-50 font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-2xl h-58" id="popover-repo-left-purple" style={{zIndex: 2}}>
                <div>
                    <div id="popover-repo-Title" className="bg-indigo-600 text-white opacity-75 font-semibold p-3 mb-0 border-b border-solid border-blueGray-100 uppercase rounded-t-2xl py-3">
                        <span id="popover-repo-TitleContent"></span>
                        <button className="float-right" onClick={closeRepoPopover}>X</button>
                    </div>
                    <div id="popover-repo-Content" className="text-white px-6 py-4 h-2/3 overflow-y-scroll h-28"></div>
                    <div id="profile-repo-Button" className="text-white px-6 py-4"></div>
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

    const FormDiv = (handleSubmit, openRepoPopover, commentText) => {
        return (
            <div className="py-1 bg-blue-500 rounded-3xl px-20 shadow-[1.0px_1.0px_2.0px_1.0px_rgba(0,0,0,0.58)]">
                <form onSubmit={handleSubmit}>
                    <h1 id="title_element" className="self-center text-center text-white text-xl text-center font-semibold font-mono mb-1 mt-3">Enter
                        Github Data
                    </h1>
                    <div className="self-center mb-4 mt-2">
                        <div className="py-2 px-10 mx-0 min-w-full flex flex-col items-center">
                            <textarea id="prompt_input" cols="38" rows="13" className="self-center py-2 border-2 bg-slate-100 shadow-[1.5px_2.0px_1.0px_0.5px_rgba(0,0,0,0.28)] border-gray-200 w-90 h-78 sm:w-90 text-xs font-sm break-words tracking-wide text-blue-600 placeholder-white border rounded-3xl focus:shadow-outline" value={commentText} onChange={e => setCommentText(e.target.value)}>
                            </textarea>
                        </div>
                        <div className="px-10 mx-0 min-w-full flex flex-col items-center">
                            <button id="submit_prompt_btn" className="w-80 sm:w-90 bg-slate-100 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:bg-blue-400 text-blue-500 hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2" type="submit">
                                Generate
                            </button>
                            <p></p>
                            <button className="w-80 sm:w-90 bg-slate-100 hover:bg-blue-400 text-blue-500 shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:text-white hover:border-gray-200 text-lg font-semibold py-2 px-5 rounded-2xl mt-2" onClick={(e) => openRepoPopover(e)} type="button">Repos</button>
                        </div>
                    </div>
                </form>
            </div>
        )
    }

    return (
        <div>
            <h1 id="h1content" className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-10 pb-2 mb-2 pt-8 mx-30 px-20">
                Generate Team Report From Metadata
            </h1>
            {repoPopoverUI()}
            <div id="topRow" className="grid grid-cols-3 gap-10 rounded-3xl mx-20 mt-6">
                <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
                    {FormDiv(handleSubmit, openRepoPopover, commentText)}
                </div>
                <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
                    <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                        <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Summary</h1>
                        <div id="summary" className="px-4 mx-0 mb-3 mt-2">
                            {isOpened && (
                                <div id="summary-container" className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] overflow-y-scroll h-100 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3 pt-6 pb-20">
                                    {ShowSummary(teamData["report"])}
                                    {ShowHighlights(teamData["report"])}
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
                        {isOpened && (
                            <div className="content-center py-1 h-90 rounded-3xl mb-4 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] mx-1 px-3">
                                {ShowTeamList(teamData["team"], openPopover)}
                            </div>
                        )}
                    </div>
                </div>
            </div>
            {isOpened && (
                <GraphicsUI/>
            )}
        </div>
    );
};

const domContainer = document.querySelector('#root');
ReactDOM.render(<TeamReport/>, domContainer);
