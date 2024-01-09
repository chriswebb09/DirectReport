const { useState, useEffect } = React;

const RememberMe = () => {
    return (
        <div className="flex items-start">
            <div className="flex items-center h-5">
                <input id="remember" name="remember" aria-describedby="remember" type="checkbox" className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800" required=""/>
            </div>
            <div className="ml-3 text-sm">
                <label htmlFor="remember" className="text-white dark:text-gray-300">
                    Remember me
                </label>
            </div>
        </div>
    )
}

const NameElement = (props) => {
    console.log(props);
    return (
        <div>
            <label htmlFor={props.forHtml} className="block mb-2 text-sm font-semibold tracking-wider text-white dark:text-white">
                {props.labelText}
            </label>
            <input type={props.type} name={props.name} id={props.id} className="bg-gray-50 border border-gray-300 text-blue-500 tracking-wider sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 font-semibold shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)]" placeholder={props.placeholder} required="" value={props.value}/>
        </div>
    )
}

const AccountForm = (action, submit_button, showBox, userProfile) => {
    const actionElem = action.action;
    const submit_buttonElem = submit_button.button_title;
    let props;
    let emailProps;
    let lastNameProps;
    let firstNameProps;
    let userNameProps;
    emailProps = {
        type: "email",
        forHtml: "email",
        labelText: "Email",
        name: "email",
        id: "email",
        placeholder: "name@company.com",
        value: (userProfile.data !== undefined && userProfile.data["user"]["email"] != null) ? userProfile.data["user"]["email"] : "name@company.com"
    }
    firstNameProps = {
        type: "text",
        forHtml: "firstname",
        labelText: "First name",
        name: "firstname",
        id: "firstname",
        placeholder: "John",
        value: (userProfile.data !== undefined && userProfile.data["user"]["firstname"] != null) ? userProfile.data["user"]["firstname"] : "John"
    }
    lastNameProps = {
        type: "text",
        forHtml: "lastname",
        labelText: "Last name",
        name: "lastname",
        id: "lastname",
        placeholder: "Doe",
        value: (userProfile.data !== undefined && userProfile.data["user"]["lastname"] != null) ? userProfile.data["user"]["lastname"] : "Doe"
    }
    userNameProps = {
        type: "text",
        forHtml: "username",
        labelText: "Username",
        name: "username",
        id: "username",
        placeholder: "JohnDoe",
        value: (userProfile.data !== undefined && userProfile.data["user"]["username"] != null) ? userProfile.data["user"]["username"] : "JohnDoe"
    }
    return (
        <form className="space-y-4 md:space-y-6" method="POST" action={actionElem}>
            {NameElement(props = emailProps)}
            {NameElement(props = firstNameProps)}
            {NameElement(props = lastNameProps)}
            {NameElement(props = userNameProps)}
            {NameElement(props = {
                type: "password",
                forHtml: "password",
                labelText: "Password",
                name: "password",
                id: "password",
                placeholder: "••••••••",
                value: "••••••••"
            })}
            {showBox.showBox && (
                <div className="flex items-center justify-between">
                    {RememberMe()}
                </div>
            )}
            <div className="flex items-center justify-center py-4">
                <button type="submit" className="w-full text-blue-600 bg-white hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-mono tracking-wide font-semibold rounded-3xl text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)]">
                    {submit_buttonElem}
                </button>
            </div>

        </form>
    )
}

const UserAccount = ({action, header, button_title, data}) => {
    return (
        <div>
            <div className="flex flex-col items-center justify-center pt-4">
                <div className="w-1/2 px-20 mx-20">
                    <div className="mx-30 bg-blue-500 rounded-3xl shadow dark:border dark:bg-gray-800 dark:border-gray-700 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)]">
                        <div className="py-2 space-y-4 md:space-y-6 sm:p-8">
                            <h1 className="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl dark:text-white">
                                {header}
                            </h1>
                            {AccountForm({action}, {button_title}, {showBox: false}, {data})}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
