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
            console.log(res.json());
            return res.json();
        }).then(function(data) {
            setGeneratedEmail(data["email"]);
            toggleHide();
        });
    }

    const openPopover = e => {
        e.preventDefault()
        let element = e.target;
        while(element.nodeName !== "BUTTON") {
            element = element.parentNode;
        }
        Popper.createPopper(element, document.getElementById('popover-id-left-purple'), {
            strategy: 'fixed'
        });
        document.getElementById('popover-id-left-purple').classList.toggle("hidden");
    }

    // function showGraphics(){
    //     const mapcontainer = d3.select("#map-container");
    //     mapcontainer.append("span").text("Hello, world!");
    // }

    function stringify (x) {
        console.log(Object.prototype.toString.call(x));
    }
    // function showGraphics(data) {
    //     var newData = data
    //     var stringData = JSON.stringify(newData['shortlog']);
    //
    //     stringify(newData)
    //     console.log(stringData)
    //     var values = Object.keys(newData['shortlog']).map(function(key){
    //         return Number(newData['shortlog'][key]);
    //     });
    //     console.log(values);
    //     var dataset = values
    //         // [5, 2, 10, 15, 20, 25]
    //
    //     var chartWidth = 240
    //     var chartHeight = 120
    //     var padding = 20
    //     var heightScalingFactor = chartHeight / getMax(dataset)
    //
    //     var svg = d3
    //         .select('#map-container')
    //         .append('svg')
    //         .attr('width', chartWidth)
    //         .attr('height', chartHeight)
    //
    //     svg.selectAll('rect')
    //         .data(dataset)
    //         .enter()
    //         .append('rect')
    //         .attr('x', function (value, index) {
    //             return (index * (chartWidth / dataset.length)) + padding
    //         })
    //         .attr('y', function (value, index) {
    //             return chartHeight - (value * heightScalingFactor)
    //         })
    //         .attr('width', (chartWidth / dataset.length) - padding)
    //         .attr('height', function (value, index) {
    //             return value * heightScalingFactor
    //         })
    //         .attr('fill', 'pink')
    //
    //     /**
    //      *  Gets the maximum value in a collection of numbers.
    //      */
    //
    // }
    //
    // function getMax(collection) {
    //     var max = 0
    //     collection.forEach(function (element) {
    //         max = element > max ? element : max
    //     })
    //     return max
    // }
    //

    return (
        <div>
            <h1 class="self-center text-center text-4xl text-indigo-800 tracking-wide text-center font-black mb-6 mt-5 mx-20 px-20">Generate
                Team Report From Metadata</h1>
            <div className="grid grid-cols-3 gap-10 mt-10 mb-20 mx-10">
                <div className="col-span-1 justify-center my-10" id="edit_summary_div">
                    <div className="shadow-lg py-1 border-4 bg-blue-500 rounded-2xl px-30 mb-10">
                        <form class="py-2" onSubmit={handleSubmit}>
                            <h1 class="self-center text-center text-white tracking-wide text-2xl text-center font-bold mb-4 mt-6">Enter
                                Github Data</h1>
                            <div className="self-center mb-6 mt-5">
                                <div className="py-4 px-10 mx-0 min-w-full flex flex-col items-center">
                                    <textarea id="prompt_input" cols="30" rows="13"
                                              class="self-center border-4 border-white w-90 sm:w-90 text-base tracking-wide text-indigo-700 placeholder-white border rounded-2xl focus:shadow-outline"
                                              value={commentText}
                                              onChange={e => setCommentText(e.target.value)}></textarea>
                                </div>
                                <div className="px-10 mx-0 min-w-full flex flex-col items-center">
                                    <button id="submit_prompt_btn"
                                            class="shadow-md w-80 sm:w-90 tracking-wide bg-white hover:bg-blue-700 text-indigo-700 hover:text-white border-4 border-indigo-700 hover:border-gray-200 text-xl font-semibold py-4 px-10 rounded-lg mt-10"
                                            type="submit">Generate
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div id="show_summmary_div" className="col-span-1 justify-center my-10">
                    <div className="shadow-lg py-3 border-4 bg-blue-500 rounded-2xl px-30 mb-10">
                        <h1 class="self-center text-center text-2xl tracking-wide text-white text-center font-bold mb-6 mt-5 mx-20 px-20">Summary</h1>
                        <div id="summary" className="px-2 mx-0 mb-8 mt-8">
                            {isOpened && (
                                <div id="summary-container"
                                     className="bg-white ml-3 mr-3 overflow-y-scroll h-90 rounded-2xl border-4 border-gray tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-10 mb-14 px-1 py-4">
                                    <p id="show_summary" class="w-97 sm:w-97 overflow-y-auto break-words">
                                        {teamData["report"] !== undefined ?
                                            <div
                                                className="my-7 px-2 text-sm tracking-wide text-blue-700">{teamData["report"]["summary"]}</div>
                                            : null
                                        }
                                    </p>
                                    <div className="h-80">
                                        <ul className="px-2">
                                            {teamData["report"] &&
                                                teamData["report"]["highlights"].map(hightlight =>
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
                <div id="team_member_to_select" className="col-span-1 justify-center my-10">
                    <div className="shadow-lg py-1 border-4 bg-blue-500 rounded-2xl px-4 mb-9">
                        <h1 class="self-center text-center text-2xl tracking-wide text-white text-center font-bold mb-6 mt-8 mx-20 px-20">
                            Team</h1>
                        <div
                            className="hidden bg-purple-600 border-0 mr-3 block z-50 font-normal leading-normal text-sm max-w-xs text-left no-underline break-words rounded-lg"
                            id="popover-id-left-purple">
                            <div>
                                <div
                                    className="bg-purple-600 text-white opacity-75 font-semibold p-3 mb-0 border-b border-solid border-blueGray-100 uppercase rounded-t-lg">purple
                                    popover title
                                </div>
                                <div className="text-white p-10">And here's some amazing content. It's very engaging.
                                    Right?
                                </div>
                            </div>
                        </div>
                        <div id="display_team" className="mb-6 my-9"></div>
                        {isOpened && (
                            <div
                                className="content-center py-2 h-90 rounded-2xl ml-3 mb-12 border-4 bg-slate-100 mx-2 px-2">
                                <div className="items-center my-6 mx-2 px-2 select-none">
                                    {teamData["team"] &&
                                        teamData["team"].map(teammember =>
                                                // <form class="py-2 px-2" onSubmit={handleSubmit}>
                                                <button
                                                    class="bg-blue-600 py-1 px-3 pb-2 pt-2.5 mr-2 my-2 shadow-md no-underline rounded-full text-white font-sans border-2 border-gray font-medium text-sm btn-primary hover:text-white hover:bg-indigo-700 focus:outline-none active:shadow-none"
                                                    onClick={openPopover}>{teammember.name}</button>
                                            // </form>
                                        )}
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
            <div className="grid grid-cols-3 gap-10 mt-10 mb-20 mx-10 border-4 border-indigo-700 rounded-2xl px-30">
                <div className="col-span-1 justify-center my-10 border-4 border-indigo-700 rounded-2xl px-30 ml-10" id="dd">
                    <div className="col-span-1 justify-center my-10 px-5" id="data_display_div">
                        <div className="border-4 rounded-2xl px-2 mx-5 mb-8 mt-8">
                            <div id="map-container" className="py-5"></div>
                        </div>
                    </div>
                </div>
                <div className="col-span-1 justify-center my-10  border-4 border-indigo-700 rounded-2xl px-30 mx-5" id="dd">
                    <div className="col-span-1 justify-center my-10" id="data_display_div-r">
                        <div id="new" className="border-4 rounded-2xl px-30 px-2 mx-0 mb-8 mt-8">
                            <div id="map-con"></div>
                        </div>
                    </div>
                </div>
                <div className="col-span-1 justify-center my-10  border-4 border-indigo-700 rounded-2xl px-30 mr-10" id="dd">
                    <div className="col-span-1 justify-center my-10" id="data_display_div-rr">
                        <div id="newr" className="border-4 rounded-2xl px-30 px-2 mx-0 mb-8 mt-8">
                            <div id="map-corn"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    );
};

const domContainer = document.querySelector('#root');
ReactDOM.render(<TeamData/>, domContainer);
