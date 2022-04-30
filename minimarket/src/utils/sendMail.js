import nodemailer from "nodemailer"

const trasporter = nodemailer.createTransport({
    host : "smtp.gmail.com",
    port : 587,
    auth:{
        user: "elnixo0007@gmail.com",
        pass: "hqxwryzrtengydns",
    },
});

export const enviarCorreoValidacion = ({destinatario, hash})=>{

    const html =`
    <p>
        parrafo 
        <a href="https://www.google.com">
         valida mi cuenta
        </a>
    </p>
    `;
    try{
    trasporter.sendMail({
        from: "danny.cerda@outlook.com",
        to: destinatario,
        subject:"validacion de correo minimarket",
        html,
    });
    console.log("correo enviado exitosamente");
    }catch(error){
        console.log(error);
        return error;
    }


};