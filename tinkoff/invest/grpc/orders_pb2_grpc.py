# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tinkoff.invest.grpc import (
    orders_pb2 as tinkoff_dot_invest_dot_grpc_dot_orders__pb2,
)


class OrdersStreamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TradesStream = channel.unary_stream(
                '/tinkoff.public.invest.api.contract.v1.OrdersStreamService/TradesStream',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.TradesStreamRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.TradesStreamResponse.FromString,
                )
        self.OrderStateStream = channel.unary_stream(
                '/tinkoff.public.invest.api.contract.v1.OrdersStreamService/OrderStateStream',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderStateStreamRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderStateStreamResponse.FromString,
                )


class OrdersStreamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TradesStream(self, request, context):
        """Stream сделок пользователя
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderStateStream(self, request, context):
        """Stream поручений пользователя. Перед работой прочитайте [статью](https://russianinvestments.github.io/investAPI/orders_state_stream/).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrdersStreamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TradesStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TradesStream,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.TradesStreamRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.TradesStreamResponse.SerializeToString,
            ),
            'OrderStateStream': grpc.unary_stream_rpc_method_handler(
                    servicer.OrderStateStream,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderStateStreamRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderStateStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.OrdersStreamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrdersStreamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TradesStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersStreamService/TradesStream',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.TradesStreamRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.TradesStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderStateStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersStreamService/OrderStateStream',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderStateStreamRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderStateStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class OrdersServiceStub(object):
    """Сервис предназначен для работы с торговыми поручениями:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение статуса;</br> **4**.
    расчёт полной стоимости;</br> **5**. получение списка заявок.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PostOrder = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OrdersService/PostOrder',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderResponse.FromString,
                )
        self.CancelOrder = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OrdersService/CancelOrder',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.CancelOrderRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.CancelOrderResponse.FromString,
                )
        self.GetOrderState = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OrdersService/GetOrderState',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderStateRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderState.FromString,
                )
        self.GetOrders = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OrdersService/GetOrders',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrdersRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrdersResponse.FromString,
                )
        self.ReplaceOrder = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OrdersService/ReplaceOrder',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.ReplaceOrderRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderResponse.FromString,
                )
        self.GetMaxLots = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OrdersService/GetMaxLots',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetMaxLotsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetMaxLotsResponse.FromString,
                )
        self.GetOrderPrice = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OrdersService/GetOrderPrice',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderPriceRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderPriceResponse.FromString,
                )


class OrdersServiceServicer(object):
    """Сервис предназначен для работы с торговыми поручениями:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение статуса;</br> **4**.
    расчёт полной стоимости;</br> **5**. получение списка заявок.
    """

    def PostOrder(self, request, context):
        """Метод выставления заявки.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOrder(self, request, context):
        """Метод отмены биржевой заявки.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderState(self, request, context):
        """Метод получения статуса торгового поручения.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrders(self, request, context):
        """Метод получения списка активных заявок по счёту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaceOrder(self, request, context):
        """Метод изменения выставленной заявки.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMaxLots(self, request, context):
        """расчет количества доступных для покупки/продажи лотов
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderPrice(self, request, context):
        """Метод получения предварительной стоимости для лимитной заявки
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrdersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PostOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.PostOrder,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderResponse.SerializeToString,
            ),
            'CancelOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOrder,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.CancelOrderRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.CancelOrderResponse.SerializeToString,
            ),
            'GetOrderState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderState,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderStateRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderState.SerializeToString,
            ),
            'GetOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrders,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrdersRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrdersResponse.SerializeToString,
            ),
            'ReplaceOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaceOrder,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.ReplaceOrderRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderResponse.SerializeToString,
            ),
            'GetMaxLots': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMaxLots,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetMaxLotsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetMaxLotsResponse.SerializeToString,
            ),
            'GetOrderPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderPrice,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderPriceRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderPriceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.OrdersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrdersService(object):
    """Сервис предназначен для работы с торговыми поручениями:</br> **1**.
    выставление;</br> **2**. отмена;</br> **3**. получение статуса;</br> **4**.
    расчёт полной стоимости;</br> **5**. получение списка заявок.
    """

    @staticmethod
    def PostOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersService/PostOrder',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersService/CancelOrder',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.CancelOrderRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.CancelOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersService/GetOrderState',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderStateRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.OrderState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersService/GetOrders',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrdersRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplaceOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersService/ReplaceOrder',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.ReplaceOrderRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.PostOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMaxLots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersService/GetMaxLots',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetMaxLotsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetMaxLotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OrdersService/GetOrderPrice',
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderPriceRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_orders__pb2.GetOrderPriceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)