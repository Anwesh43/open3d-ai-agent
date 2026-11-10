from agents.open3d_agent import create3DShapes 
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(create3DShapes(prompt))