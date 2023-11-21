'use strict';
const elem = React.createElement;

class Home extends React.Component {
    render() {
        return elem(
            'div',
            null,
            React.createElement(
                'div',
                {
                    className: "py-24 flex h-100",
                    style: {background: "linear-gradient(90deg, #667eea 0%, #764ba2 100%)"}
                },
                React.createElement(
                    "div",
                    {
                        className: "container mx-auto px-6"
                    },
                    React.createElement(
                        "h2",
                        {
                            className: "my-4 text-4xl font-bold mb-2 text-white"
                        },
                        "DirectReport."
                    ),
                    React.createElement(
                        "h3",
                        {
                            className: "my-8 text-2xl mb-12 text-gray-200"
                        },
                        "Keep track of your accomplishments each day of the workweek."
                    ),
                    React.createElement(
                        "div",
                        {
                            className: "my-8"
                        },
                        React.createElement(
                            "a",
                            {
                                className: "my-12 px-14 py-5 text-lg font-bold text-center text-white bg-gray-400 rounded-full hover:bg-blue-800 shadow-lg uppercase",
                                href: "https://github.com/chriswebb09/DirectReport"
                            },
                            "Github"
                        )
                    )
                )
            )
        );
    }
}

const domContainer = document.querySelector('#root');
ReactDOM.render(elem(Home), domContainer);
