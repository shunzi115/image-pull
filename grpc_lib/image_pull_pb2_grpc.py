# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpc_lib.image_pull_pb2 as image__pull__pb2


class ImagePullStub(object):
  """The ImagePull service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CheckImageExists = channel.unary_unary(
        '/ImagePull/CheckImageExists',
        request_serializer=image__pull__pb2.ImageName.SerializeToString,
        response_deserializer=image__pull__pb2.Results.FromString,
        )
    self.PullImage = channel.unary_unary(
        '/ImagePull/PullImage',
        request_serializer=image__pull__pb2.ImageName.SerializeToString,
        response_deserializer=image__pull__pb2.Results.FromString,
        )


class ImagePullServicer(object):
  """The ImagePull service definition.
  """

  def CheckImageExists(self, request, context):
    """Sends a Query
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PullImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImagePullServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CheckImageExists': grpc.unary_unary_rpc_method_handler(
          servicer.CheckImageExists,
          request_deserializer=image__pull__pb2.ImageName.FromString,
          response_serializer=image__pull__pb2.Results.SerializeToString,
      ),
      'PullImage': grpc.unary_unary_rpc_method_handler(
          servicer.PullImage,
          request_deserializer=image__pull__pb2.ImageName.FromString,
          response_serializer=image__pull__pb2.Results.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ImagePull', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
