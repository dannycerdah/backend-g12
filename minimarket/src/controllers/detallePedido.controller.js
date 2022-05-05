import {Prisma} from '../prisma.js'
import { crearDetallePedidoRequestDTO } from '../dtos/detallePedido.dto.js';

export const crearDetallePedido = async(req,res)=>{
   try{   
        const data = crearDetallePedidoRequestDTO(req.body);
        
        await Prisma.$transaction(async () => {
            const { precio }  = await Prisma.producto.findUnique({
                where : {id: data.productoId},
                rejectOnNotFound: false,
                select: {precio: true},
            });

            const {id,total} = await Prisma.pedido.findUnique({
                where: { id: data.pedidoId},
                select: {id:true,total:true},
                rejectOnNotFound:true,  
            });

            const { subtotal } = await Prisma.detallePedido.create({
                data:{ ...data, subTotal:precio * data.cantidad},
                select:{subtotal:true},
            });
             
            await Prisma.pedido.update({
                data:{total:total + subtotal},
                where:{id},
            })

        })
        return res.status(201).json({
            message: "Error al crear el detalle del pedido",
            content: error.message,
        });
    } catch(error){
        return res.status(400).json({
            message : "Error al crear el detalle del pedido",
            content: error.message
        });
    }
};