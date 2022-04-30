import express, { json } from 'express';
import {productosRouter} from "./routes/productos.router.js"
import { usuarioRouter } from './routes/usuarios.router.js';
const app = express();

app.use(json());

const PORT = process.env.PORT ?? 3000;

app.get("/",(req,res)=>{
    res.json({
        message: "Bienvenido a mi API del minimarket"
    });
});

app.use(productosRouter);
app.use(usuarioRouter);

app.listen(PORT, () =>{
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
})