const { useState, useEffect } = React;

class SavedReportList extends React.Component {
    render() {
        return (
            <div className="mx-20 pb-5 pt-5">
                <h1 className="text-2xl text-blue-800 text-left font-bold font-mono mb-2 mx-10">
                    Saved Reports
                </h1>
                <div className="grid grid-cols-3 gap-4 mb-20 mx-30">
                    {this.props.listdata.map(item =>
                        <div className="col-span-1 justify-center mt-1 mb-1">
                            <article className="mx-4 mt-2 w-90 rounded-3xl bg-white p-1 shadow-[1.0px_1.0px_2.0px_1.0px_rgba(0,0,0,0.58)]">
                                <a className="block rounded-xl bg-white sm:p-6 lg:p-8" href={'/reports/' + item.uuid}>
                                    <div>
                                        <h2 className="text-2xl font-bold text-gray-800 sm:text-xl">{'User: ' + item.user_id}</h2>
                                        <p className="mt-3 text-sm text-justify line-clamp-3 text-gray-500">{'Raw Input: ' + item.raw_input}</p>
                                    </div>
                                </a>
                            </article>
                        </div>
                    )}
                </div>
            </div>
        );
    }
}

class EmptyEntryList extends React.Component {
    render() {
        return (
            <div className="mx-50 content-center mt-20 my-28 h-150">
                <div className="flex flex-col justify-center my-6 mx-60">
                    <h1 className="self-center text-3xl text-gray-700 text-center font-bold">Add New Entry</h1>
                    <EntryForm/>
                </div>
            </div>
        );
    }
}
