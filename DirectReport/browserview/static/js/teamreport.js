const { useState, useEffect } = React;

const TeamData = () => {

    const [teamData, setTeamData] = useState({});
    const [commentText, setCommentText] = useState("")
    const [isOpened, setIsOpened] = useState(false);
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
        document.getElementById('popoverTitleContent').innerHTML = teammember.name
        document.getElementById('popoverContent').innerHTML = teammember.accomplishments;
        document.getElementById('popoverCommits').innerHTML = "Commits: " + teammember.commits;
    }

    const openRepoPopover = (e: ChangeEvent<HTMLInputElement>) => {
        const element = document.getElementById('formUI');
        Popper.createPopper(element, document.getElementById('popover-repo-left-purple'), {
            strategy: 'fixed',
            modifiers: [{
                name: "offset",  // offsets popper from the reference/button
                options: {
                    offset: [0, 8]
                }
            }, {
                name: "flip", // flips popper with allowed placements
                options: {
                    allowedAutoPlacements: ["right", "left", "top", "bottom"],
                    rootBoundary: "viewport"
                }
            }]
        });
        document.getElementById('popover-repo-left-purple').classList.toggle("hidden");
        document.getElementById('popover-repo-TitleContent').innerHTML = "Repos" + "(" + teamData["repos"].length + ")";
        var list = '<ul className="px-30 py-30">';
        for (var i = 0; i < teamData["repos"].length; i++) {
            list += '<li>' + '<a href=/repo/' + teamData["repos"][i] + '>' + teamData["repos"][i] + '' + '</li>';
        }
        list += '</ul>';
        document.getElementById('popover-repo-Content').innerHTML = list;
    }

    const repoPopoverUI = () => {
        return (
            <div className="hidden bg-indigo-600 border-0 mr-3 block z-50 font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-lg" id="popover-repo-left-purple" style={{zIndex: -1}}>
                <div>
                    <div id="popover-repo-Title" className="bg-indigo-600 text-white opacity-75 font-semibold p-3 mb-0 border-b border-solid border-blueGray-100 uppercase rounded-t-lg py-3">
                        <span id="popover-repo-TitleContent"></span>
                        <button className="float-right" onClick={closeRepoPopover}>X</button>
                    </div>
                    <div id="popover-repo-Content" className="text-white px-6 py-4"></div>
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

    const ShowSummary = (report) => {
        return (
            <p id="show_summary" className="w-97 sm:w-97 overflow-y-auto break-words">
                {report !== undefined ?
                    <div className="px-2 mb-1 text-xs text-blue-700">
                        {report["summary"]}
                    </div> : null
                }
            </p>
        )
    }

    return (
        <div>
            <h1 className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-3 pb-2 mb-2 pt-4 mx-10 px-20">
                Generate Team Report From Metadata
            </h1>
            {/*{repoPopoverUI()}*/}
            <div id="topRow" className="grid grid-cols-3 gap-8 rounded-3xl mx-10 mt-6">
                <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
                    {FormDiv(handleSubmit, openRepoPopover, commentText)}
                </div>
                <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
                    <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.48)]">
                        <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Summary</h1>
                        <div id="summary" className="px-4 mx-0 mb-3 mt-2">
                            {isOpened && (
                                <div id="summary-container" className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.28)] overflow-y-scroll h-100 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3 pt-6 pb-20">
                                    {ShowSummary(teamData["report"])}
                                    {ShowHighlights(teamData["report"])}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
                <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center">
                    <div className="pb-6 pt-2 bg-blue-500 rounded-3xl px-4 mb-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.48)]">
                        <h1 className="self-center text-center text-xl text-white text-center font-semibold font-mono mb-1 mt-2 mx-20 px-20">Team</h1>
                        <PopoverUI closePopover={closePopover}/>
                        <div id="display_team" className="my-3"></div>
                        {isOpened && (
                            <div className="content-center py-1 h-90 rounded-3xl mb-4 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.28)] mx-1 px-3">
                                {ShowTeamList(teamData["team"], openPopover)}
                            </div>
                        )}
                    </div>
                </div>
            </div>
            {isOpened && (
                <div>
                    <h3 className="text-xl text-blue-800 text-left font-mono font-semibold mt-10 mb-5 mx-5 px-12">Data</h3>
                    <GraphDiv/>
                </div>
            )}
        </div>
    );
};

const domContainer = document.querySelector('#root');
ReactDOM.render(<TeamData/>, domContainer);
