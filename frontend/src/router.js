import {createBrowserRouter, Navigate} from "react-router-dom";
// import * as path from "node:path";
import {MainLayout} from "./layouts/MainLayout";
import {LoginPage} from "./pages/LoginPage";
import {CarPage} from "./pages/CarPage";
import {RegisterPage} from "./pages/RegisterPage";

const router = createBrowserRouter([
    {path:'', element:<MainLayout/>, children:[
            {
                index:true, element:<Navigate to={'login'}/>
            },
            {
                path:'login', element:<LoginPage/>
            },
            {
                path:'cars', element:<CarPage/>
            },
            {
                path:'registration', element:<RegisterPage/>
            }
        ]}
]);

export {
    router
}