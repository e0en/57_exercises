import System.IO

prompt = do
  putStr "What is your name? "
  hFlush stdout
  getLine

messageFor = ("Hello, " ++) . (++ ", nice to meet you!")

main = fmap messageFor prompt >>= putStrLn
