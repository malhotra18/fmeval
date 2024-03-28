from opentelemetry import baggage, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")

with tracer.start_as_current_span("foo"):
    current_span = trace.get_current_span()

    current_span.set_attribute("operation.value", 1)
    current_span.set_attribute("operation.name", "Saying hello!")
    current_span.set_attribute("operation.other-stuff", [1, 2, 3])
    print("Hello World!")

with tracer.start_as_current_span("bar"):
    print("Hello World again!")
    with tracer.start_as_current_span("child") as child:
        # do some work that 'child' tracks
        print("doing some nested work...")