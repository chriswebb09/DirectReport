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
        });
    };

    function toggle() {
        setIsOpened(wasOpened => !wasOpened);
    }

    function toggleHide() {
        setIsHidden(wasHidden => !wasHidden);
    }


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

    return (
        <div>
            <h1 class="self-center text-center text-4xl text-indigo-800 tracking-wide text-center font-black mb-14 mx-20 px-20">Generate Team Report From Metadata</h1>
            <div class="grid grid-cols-3 gap-10 mt-10 mb-20 mx-20">
                <div class="col-span-1 justify-center my-10" id="edit_summary_div">
                    <div class="shadow-lg py-1 border-4 border-indigo-600 rounded-2xl px-30 mb-10">
                        <form class=" py-2 px-2" onSubmit={handleSubmit}>
                            <h1 class="self-center text-center text-indigo-700 tracking-wide text-2xl text-center font-bold mb-4 mt-6">Enter Github Data</h1>
                            <div class="self-center mb-6 mt-5">
                                <div class="py-4 px-10 mx-0 min-w-full flex flex-col items-center">
                                    <textarea id="prompt_input" cols="40" rows="13" class="self-center border-4 border-indigo-700 w-90 sm:w-90 text-base tracking-wide text-indigo-700 placeholder-white border rounded-2xl focus:shadow-outline" value={commentText}  onChange={e => setCommentText(e.target.value)} ></textarea>
                                </div>
                                <div class="px-10 mx-0 min-w-full flex flex-col items-center">
                                    <button id="submit_prompt_btn" class="shadow-md w-80 sm:w-90 tracking-wide bg-white hover:bg-indigo-700 text-indigo-700 hover:text-white border-4 border-indigo-700 hover:border-gray-200 text-xl font-semibold py-4 px-10 rounded-lg mt-10"  type="submit">Generate</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div id="show_summmary_div" class="col-span-1 justify-center my-10">
                    <div class="shadow-lg border-4 border-indigo-700 rounded-2xl px-30 mb-10">
                        <h1 class="self-center text-center text-2xl tracking-wide text-indigo-700 text-center font-bold mb-10 mt-10 mx-20 px-20">Summary</h1>
                        <div id="summary" class="px-5 mx-0 mb-9 mt-9">
                            {isOpened && (
                                <div id="summary-container" class="bg-white ml-10 mr-10 overflow-y-scroll h-90 rounded-2xl border-4 border-indigo-700 tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-8 mb-14 px-1 py-4">
                                    <p id="show_summary" class="w-90 sm:w-90 overflow-y-auto break-words">
                                        { teamData["report"] !== undefined ?
                                            <div className="my-7 px-5 text-lg tracking-wide text-indigo-700">{teamData["report"]["summary"]}</div>
                                            : null
                                        }
                                    </p>
                                    <div class="h-80">
                                        <ul className="px-5">
                                            {teamData["report"] &&
                                                teamData["report"]["highlights"].map(hightlight =>
                                                    <li className="mb-3">
                                                        <h3 className="font-bold text-lg mb-1 tracking-wide text-indigo-700">{hightlight.title}</h3>
                                                        <p class="w-90 sm:w-90 overflow-y-auto text-lg font-md break-words tracking-wide text-indigo-700">{hightlight.description}</p>
                                                    </li>
                                                )}
                                        </ul>
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
                <div id="team_member_to_select" class="col-span-1 justify-center my-10">
                    <div class="shadow-lg py-1 border-4 border-indigo-700 rounded-2xl px-9 mb-9">
                        <h1 class="self-center text-center text-2xl tracking-wide text-indigo-700 text-center font-bold mb-6 mt-8 mx-20 px-20">
                            Team</h1>
                        <div id="display_team" class="mb-6 my-9"></div>
                        {isOpened && (
                            <div className="content-center py-2 h-90 rounded-2xl ml-6 mb-12 border-4 border-indigo-700 mx-5 px-3">
                                <div class="items-center my-6 mx-2 px-4 select-none">
                                    {teamData["team"] &&
                                        teamData["team"].map(teammember =>
                                            <button className="py-1 px-4 pb-2 pt-2.5 mr-3 my-2 shadow-md no-underline rounded-full text-indigo-700 font-sans border-4 font-bold text-sm border-indigo-700 btn-primary hover:text-white hover:bg-indigo-700 focus:outline-none active:shadow-none">{teammember.name}</button>
                                        )}
                                </div>
                            </div>
                        )}
                    </div>
                </div>
                <div class="col-span-3 my-12 ml-10 mr-10 mb-10 mt-40">
                    <div class="shadow-lg py-3 border-4 border-indigo-700 rounded-2xl px-30">
                        <h1 class="self-center text-center text-2xl text-indigo-700 tracking-wide font-bold w-100 mb-10 mt-10">Generated Email</h1>
                        {isHidden && (
                            <div id ="text-content" class="bg-white ml-20 mr-20 rounded-2xl py-20 tracking-wide text-gray-500 md:text-md dark:text-gray-400 px-20 mx-20 my-10">
                                {generatedEmail}
                            </div>
                        )}
                        {isOpened && (
                            <div class="py-10 px-10 min-w-full flex flex-col items-center">
                                <button type="button" id="generate_email_btn" class="shadow-md w-80 sm:w-90 bg-white hover:bg-black border-4 border-indigo-700 text-indigo-700 text-xl font-semibold py-4 px-10 rounded-lg" onClick={handleClick}>Generate Email</button>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>

    );
};

const domContainer = document.querySelector('#root');
ReactDOM.render(<TeamData />, domContainer);
