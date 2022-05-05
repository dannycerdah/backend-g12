import express, { json } from "express";
import { detallePedidoRouter } from "./routes/detallePedido.router.js";
import { pedidosRouter } from "./routes/pedidos.routes.js";
import { productosRouter } from "./routes/productos.routes.js";
import { usuarioRouter } from "./routes/usuarios.routes.js";
import mercadopago from "mercadopago"


const app = express();

mercadopago.configure({
  access_token:  
  "APP_USR-8208253118659647-112521-dd670f3fd6aa9147df51117701a2082e-677408439",
  integrator_id:'dev_24c65fb163bf11ea96500242ac130004'
});

app.use(json());

const PORT = process.env.PORT ?? 3000;

app.get("/", (req, res) => {
  res.json({
    message: "Bienvenido a mi API del minimarket",
  });
});

// agregar un bloque de rutas definidas en otro archivo
app.use(productosRouter);
app.use(usuarioRouter);
app.use(pedidosRouter);

app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});