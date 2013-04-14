
import Graph

type Vertices = [Int]
-- Graph + EdgeList + Visited + Origin

data Path = Path Graph SubPath
		deriving (Eq,Show)

data SubPath = SubPath Vertices [Bool] Int
		deriving (Eq,Show)


initIntList :: Int -> Vertices -> Vertices
initIntList n as =
  let
     xs = [0]
  in
   if (length as) < n || null as
      then initIntList n (as ++ xs)
      else as

initBoolList :: Int -> [Bool] -> [Bool]
initBoolList n as =
  let
     xs = [False]
  in
    if (length as) < n || null as
       then initBoolList n (as ++ xs)
       else as
-- pathInit
--	Starts a search of a structured Path Instance
pathInit :: Path -> Path
pathInit (Path (Graph v b) (SubPath x y z) )= if z elem v
						 then depthFirst (Path (Graph v b) (SubPath (initIntList (length v) []) (initBoolList (length v) []) z))
						 else (Path (Graph [] (Bag [[]])) (SubPath [] [] 0))

-- depthFirst...
depthFirst :: Path -> Path

