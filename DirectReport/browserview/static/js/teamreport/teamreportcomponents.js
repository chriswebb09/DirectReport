const { useState, useEffect } = React;


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

const ShowHighlights = (report) => {
    return (
        <div className="h-40">
            <ul className="px-2 pt-2 pb-2">
                {report["highlights"] && report["highlights"].map(hightlight =>
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
    )
}

const ShowTeamList = (team, openPopover) => {
    return (
        <div className="items-center my-1 select-none">
            {team
                && team.map(teammember =>
                    <button class="bg-blue-600 py-1 px-2 pb-1 pt-1 mr-0.5 my-0.5 no-underline rounded-full text-white font-sans border-2 border-gray text-xs btn-primary hover:text-white hover:bg-indigo-700 focus:outline-none active:shadow-none" onClick={((e) => openPopover(e, teammember))}>{teammember.name}</button>
                )
            }
        </div>
    )
}

class GraphDiv extends React.Component {
    render() {
        return (
            <div className="grid grid-cols-3 gap-6 mt-5 mx-10 bg-blue-500 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl px-30 py-3">
                <div className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl px-30 ml-10" id="dd">
                    <div className="col-span-1 flex justify-center my-2 px-3" id="data_display_div">
                        <div id="map-container" className="pl-10 pr-5"></div>
                    </div>
                </div>
                <div className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl px-30 mx-6" id="dd">
                    <div className="col-span-1 justify-center my-2 px-3" id="data_display_div-r">
                        <div id="map-container2" className="pl-5 pr-5"></div>
                    </div>
                </div>
                <div className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl px-30 mr-10" id="dd">
                    <div className="col-span-1 justify-center my-2 px-3" id="data_display_div-rr">
                        <div id="map-container3" className="pl-5 pr-10"></div>
                    </div>
                </div>
            </div>
        )
    }
}

const GraphicsUI = () => {
    return (
        <div>
            <h3 className="text-xl text-blue-800 text-left font-mono font-semibold mt-10 mb-5 mx-5 px-12">Data</h3>
            <GraphDiv/>
        </div>
    )
}



const PopoverUI = (closePopover) => {
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