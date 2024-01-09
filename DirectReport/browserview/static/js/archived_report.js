const {useState, useEffect} = React;
const ArchivedReport = (reportDataElems) => {

    const [teamData, setTeamData] = useState([]);
    const [repos, setRepos] = useState([]);
    const [reportData, setReportData] = useState({});
    const [commits, setCommits] = useState([]);
    const [pullRequests, setPullRequests] = useState({});
    const [broadCategories, setBroadCategories] = useState({});
    const [commitNums, setCommitNums] = useState({});
    const [rawInputText, setRawInputText] = useState("");
    const [commentText, setCommentText] = useState("");


    const openRepoPopover = () => {
        console.log("open repo popover");
    }

    useEffect(() => {
        const results = reportDataElems;
        printData({results})
    }, [reportDataElems]);

    function printData(reportDataElems) {
        const obj = JSON.parse(JSON.stringify(reportDataElems));
        const test_data = JSON.parse(JSON.stringify(obj.results.data))
        setCommitNums(test_data.commit_nums);
        setPullRequests(test_data.pull_requests);
        const test_data2 = JSON.parse(JSON.stringify(obj.results.raw_input_elem))
        setRawInputText(test_data2.raw_input);
        const new_data = obj.results.reportDataElems.replace(/'/g, '"');
        const test1 = JSON.parse(new_data);
        Object.entries(test1).forEach((entry) => {
            const [key, value] = entry;
            var obj_new = JSON.parse(JSON.stringify(value));
            if (key === "team") {
                setTeamData({
                     teamData:obj_new,
                 });
            } else if (key === "report") {
                setReportData(obj_new);
            } else if (key === "commits") {
                setCommits({
                     commits:obj_new,
                 });
            } else if (key === "broad_categories") {
                setBroadCategories(obj_new);
            } else if (key == "commit_nums") {
                setCommitNums(obj_new);
            } else if (key == "pull_requests") {
                setPullRequests(obj_new);
            }
        })
    }

    return (
        <div>
            <h1 id="h1content" className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-5 mb-8 pt-8 mx-30 px-20">
                Archived Team Report
            </h1>
            <div id="topRow" className="grid grid-cols-3 gap-10 rounded-3xl mx-20 mt-6">
                {EditArchiveSummaryElem({
                    "repos": repos,
                    "commits": commits,
                    "raw_text": rawInputText
                }, {reportData}, openRepoPopover)}
                {ArchivedSummarySection(commentText, reportData)}
                {ShowArchivedTeamSection({teamData}, closePopover)}
                {showAllGraphics({"commit_nums": commitNums, "pull_requests": pullRequests, "broad_categories": broadCategories}, '#map-container', '#map-container2', '#map-container3')}
            </div>
            <GraphicsUI/>
        </div>
    )
}
