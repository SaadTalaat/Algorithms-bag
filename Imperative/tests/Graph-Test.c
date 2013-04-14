#define CATCH_CONFIG_MAIN
#include <stdio.h>
#include <stdlib.h>
#include <graph.h>
#include <check.h>

START_TEST(test_algo_graphs)
{
	vertex vertices[] = {1,2,3,4,5,6};

	graph *g;
	g = graphInit(vertices, 6);
	addEdge(g, 5,6);
	addEdge(g, 2,1);
	addEdge(g, 5, 1);
	fail_unless( vectDegree(g, 1) == 2,"vertex degree is not consistent");
	fail_unless( maxDegree(g) == 2,"Max degree is not consistent");
	fail_unless( avgDegree(g) == 1,"Avg degree is not consistent");
	fail_unless( selfLoops(g) == 0, "There's self loops, test fail");
	free(g);
}
END_TEST

Suite *
graph_suite(void)
{
	Suite *s = suite_create("Graph");
	TCase *tcore = tcase_create("Core");
	tcase_add_test(tcore, test_algo_graphs);
	suite_add_tcase(s,tcore);
	return s;
}
int
main(void)
{
	int number_failed;
	Suite *s = graph_suite();
	SRunner *sr = srunner_create(s);
	srunner_run_all(sr, CK_VERBOSE);
	number_failed = srunner_ntests_failed(sr);
	srunner_free(sr);
	return (number_failed == 0)? EXIT_SUCCESS:EXIT_FAILURE;
}
