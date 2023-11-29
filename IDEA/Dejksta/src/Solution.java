import java.util.*;

class Solution {

    static int[] dijkstra(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj, int S) {
        int[] distance = new int[V];
        boolean[] visited = new boolean[V];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[S] = 0;

        for (int i = 0; i < V - 1; i++) {
            int minDistance = Integer.MAX_VALUE;
            int minVertex = -1;

            for (int v = 0; v < V; v++) {
                if (!visited[v] && distance[v] < minDistance) {
                    minDistance = distance[v];
                    minVertex = v;
                }
            }

            visited[minVertex] = true;

            ArrayList<ArrayList<Integer>> edges = adj.get(minVertex);
            for (ArrayList<Integer> edge : edges) {
                int v = edge.get(0);
                int weight = edge.get(1);

                int temp = distance[minVertex] + weight;
                if (temp < distance[v]) {
                    distance[v] = temp;
                }
            }
        }

        return distance;
    }


}