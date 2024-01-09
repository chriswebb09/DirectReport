const EditArchiveSummaryElem = (props, state, openRepoPopover) => {
    let raw_text = props['raw_text'];
    return (
        <div className="lg:col-span-1 sm:col-span-3 justify-center" id="edit_summary_div">
            <div className="pb-6 pt-2 bg-blue-600 rounded-3xl px-6 shadow-[1.0px_1.0px_2.0px_1.0px_rgba(0,0,0,0.58)]">
                <h1 id="title_element" className="self-center text-center text-white text-xl text-center font-bold font-mono mb-1 mt-3 py-2">Github Data</h1>
                <div className="h-30 px-2 pt-2 pb-1">
                    <div className="overflow-y-scroll h-80 rounded-3xl tracking-wide bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)]">
                        {ArchivedEntry(raw_text)}
                    </div>
                </div>

            </div>
        </div>
    )
}


const ShowArchivedSummary = (report) => {
    return (
        <p id="show_summary" className="w-97 sm:w-97 overflow-y-auto break-words">
            {report &&
                <div className="px-2 mb-1 text-xs text-blue-700 px-2 pt-2 pb-3">
                    {report.summary}
                </div>
            }
        </p>
    );
};

const ArchivedEntry = (raw_input) => {
    return (
        <div className="px-2">
            <p className="text-xs font-regular break-words text-blue-600 px-4 py-2 pb-4">{raw_input}</p>
        </div>
    )
}


const ShowArchivedHighlights = (report) => {
    if (!(report !== undefined)) {
        return (
            <div className="h-30">
                <ul className="px-2 pt-2 pb-3">
                </ul>
            </div>
        )
    } else {
        return (
            <div>
                <div className="h-30">
                    <ul className="px-2 pt-2 pb-3">
                        {/* Check if 'highlights' in report is not undefined */}
                        {report["highlights"] !== undefined ?
                            // Map each highlight to an HTML structure
                            report["highlights"].map(high_light =>
                                <li className="mt-1 mb-3">
                                    <h3 className="font-bold text-xs mb-1 mt-1 text-blue-700">
                                        {high_light.title}
                                    </h3>
                                    <p className="w-90 sm:w-90 overflow-y-auto text-xs font-sm break-words tracking-wide text-blue-600">
                                        {high_light.description}
                                    </p>
                                </li>
                            ) : null // Render nothing if 'highlights' is undefined
                        }
                    </ul>
                </div>
            </div>
        )
    }

}


const ArchivedSummarySection = (commentText, reportData) => {
    console.log("ArchivedSummarySection")
    console.log(reportData);
    return (
        <div id="show_summmary_div" className="lg:col-span-1 sm:col-span-3 justify-center">
            <div className="pb-6 pt-2 bg-blue-600 rounded-3xl px-30 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                <h1 className="self-center text-center text-xl text-white text-center font-bold font-mono mb-1 mt-3 py-2 mt-2 mx-20 px-20">Summary</h1>
                <div id="summary" className="px-4 mx-0 mb-1 mt-1">
                    <div id="summary-container" className="ml-3 mr-3 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] overflow-y-scroll h-80 rounded-3xl tracking-wide text-gray-500 md:text-gl dark:text-gray-400 mt-3 px-3">
                        {ShowArchivedSummary(reportData)}
                        {ShowArchivedHighlights(reportData)}
                    </div>
                </div>
            </div>
        </div>
    )
}


const ShowArchivedTeamSection = (teamData, closePopover) => {
    console.log(teamData["teamData"]);
    return (
        <div id="team_member_to_select" className="lg:col-span-1 sm:col-span-3 justify-center">
            <div className="pb-6 pt-2 bg-blue-600 rounded-3xl px-4 mb-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                <h1 className="self-center text-center text-xl text-white text-center font-bold font-mono mb-1 mt-3 py-2 mx-20 px-20">Team</h1>
                {PopoverUI(closePopover)}
                <div
                    className="content-center py-2 h-90 rounded-3xl mb-1 bg-slate-100 shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] mx-1 mt-3 px-3">
                    {ShowArchivedTeamList(teamData["teamData"])}
                </div>
            </div>
        </div>
    )
}
const ShowArchivedTeamList = (team) => {

    if (!(team !== undefined)) {
        return (
            null
        )
    } else {
        return (
            <div class="items-center pt-1 select-none">
                {team.teamData !== undefined && team.teamData.length > 0?
                    team.teamData.map(team_member =>
                        <button class="bg-blue-600 py-1 px-2 pb-1 pt-1 mr-0.5 my-0.5 no-underline rounded-full text-white font-sans border-2 border-gray text-xs btn-primary hover:text-white hover:bg-indigo-700 focus:outline-none active:shadow-none" onClick={(event) => openPopover(event, team_member)}>{
                            team_member.name}
                        </button>
                    ) : null
                }
            </div>
        )
    }
}