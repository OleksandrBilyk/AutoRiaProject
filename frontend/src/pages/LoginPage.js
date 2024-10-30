import {useForm} from "react-hook-form";
import {authService} from "../services/authService";
import {useNavigate} from "react-router-dom";

const LoginPage = () => {
    const {handleSubmit,register} = useForm()
    const navigate = useNavigate();
    const onSubmit = async (user) =>{
        await authService.login(user)
        navigate('/cars')
    }

    return (
        <div>
            <form onSubmit={handleSubmit(onSubmit)}>
                <input type="text" placeholder={'email'} {...register('email')}/>
                <input type="text" placeholder={'password'} {...register('password')}/>
                <button>login</button>
            </form>
            <h4>for registration new user click registration button</h4>
            <button onClick={() => navigate('/registration')}>registration</button>
        </div>
    );
};

export {LoginPage};