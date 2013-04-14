
module Graph(
	     Graph(..),
	     Bag(..),
	     getBag,
	     degree,
	     addEdge,
	     maxDegree,
	     avgDegree,
	     selfLoops
	    ) where

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

-- Initalizes matrix with empty lists --
initList :: Int -> [Vertices] -> [Vertices]
initList n as = 
  let 
     xs = [[]]
  in
   if (length as) < n || null as
      then initList n (as ++ xs)
      else as

-- Array set Index function --
setIndex :: Int -> Int -> [Vertices] -> [Vertices]
setIndex n v xs = if length(xs) < n || null xs
		     then initList n xs
		     else (take (n-1) xs) ++ [(xs!!(n-1))++[v]] ++ (drop (n) xs)

-- get degree of a point --
degree :: Graph -> Int -> Int
degree (Graph _ (Bag [])) n = 0
degree (Graph x (Bag b)) n = if any (==n) x
                                then length( b!!length(fst(break (==n) (x))))
                                else 0
 
-- Maximum degree of a graph vertex --
maxDegree :: Graph -> Int
maxDegree (Graph _ (Bag [])) = 0
maxDegree (Graph g (Bag b)) = maximum (map length b)

-- Average degree of all vertices --
avgDegree :: Graph -> Int
avgDegree (Graph _ (Bag [])) = 0
avgDegree (Graph g (Bag b)) = div (sum (map length b)) (length g)

-- self Loops exists in a graph --
selfLoops :: Graph -> Int
selfLoops (Graph _ (Bag [])) = 0
selfLoops (Graph g (Bag b)) = selfLoopsHelper (Graph g (Bag (b))) 0 ((length g)-1) -- *(length g)

selfLoopsHelper (Graph g(Bag(a:b))) s n = if null b || s >= n
					   then length(filter (==(g!!s)) a)
				  	   else length(filter (==(g!!s)) a) +  (selfLoopsHelper (Graph g (Bag b)) (s+1)(n-1))
