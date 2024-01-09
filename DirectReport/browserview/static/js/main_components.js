const { useState, useEffect } = React;

const AuthSpinnerUI = () => {
    return (
        <div className="hidden rounded-2xl col-span-1" id="AuthSpinnerUI" style={{zIndex: 100}}>
            <div>
                <div role="status" className="mx-0 min-w-full flex flex-col items-center">
                    <div>
                        <svg aria-hidden="true" className="w-10 h-10 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
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

const GraphElement = (title, id, mapcontainer_id) => {
    return (
        <div>
            <h1 id="title_element" className="self-center text-center text-white text-lg text-center font-bold font-mono mb-1 mt-3 py-2">{title}</h1>
            <div className="lg:col-span-1 sm:col-span-3 justify-center mt-7 mb-7 bg-white shadow-[1.0px_1.0px_6.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl px-10 ml-5" id={id}>
                <div className="flex justify-center my-2 px-3" id="data_display_div">
                    <div id={mapcontainer_id} className="pl-2 pr-2 rounded-3xl"></div>
                </div>
            </div>
        </div>
    )
}


const GraphDiv = () => {
    return (
        <div className="grid grid-cols-3 gap-10 mt-5 mx-20 bg-blue-600 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl px-5 py-3">
            {GraphElement("Number of Pull Requests", "dd", "map-container")}
            {GraphElement("Commits Over Times", "dd", "map-container2")}
            {GraphElement("Broad Areas of Work", "dd", "map-container3")}
        </div>
    )
}

const GraphicsUI = memo(function Graphics() {
    return (
        <div>
            <h3 className="text-xl text-blue-800 font-mono font-semibold mt-10 mb-8 mx-10 px-12">Graphic Data</h3>
            <GraphDiv/>
        </div>
    )
})
