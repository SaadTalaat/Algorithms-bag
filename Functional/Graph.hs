

-- A simple Graph --

type Vertices = [Int] 

data Bag = Bag [Vertices]
		deriving (Eq,Show)

data Graph = Graph Vertices Bag
		deriving (Eq,Show)


-- Get Bags --
getBag :: Graph -> Bag
getBag(Graph v b) = b

-- Get Bag Vertices --
getBVertices :: Bag -> [Vertices]
getBVertices (Bag v) = v

-- Get Graph Vertices --
getGVertices :: Graph -> Vertices
getGVertices(Graph v _) = v

-- Adding edges between vertices --
-- Takes numbers of adjecent indexes --
-- sets their bags to each others --
addEdge :: Graph -> Int -> Int -> Graph
addEdge (Graph x b) v w = Graph x (Bag (setIndex w v(setIndex v w (initList (length x) (getBVertices b)))) )

initList :: Int -> [Vertices] -> [Vertices]
initList n as = 
  let 
     xs = [[]]
  in
   if (length as) < n || null as
      then initList n (as ++ xs)
      else as

setIndex :: Int -> Int -> [Vertices] -> [Vertices]

setIndex n v xs = if length(xs) < n || null xs
		     then initList n xs
		     else (take (n-1) xs) ++ [[v]] ++ (drop (n) xs)

