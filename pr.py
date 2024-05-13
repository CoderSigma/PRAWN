import marshal

# Load the serialized bytecode from the encrypted .pyc file
with open('log.pyc', 'rb') as f:
    serialized_data = f.read()

# Deserialize the bytecode
bytecode = marshal.loads(serialized_data)

# Execute the bytecode
exec(bytecode)
