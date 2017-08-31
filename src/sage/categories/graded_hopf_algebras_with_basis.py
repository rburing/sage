r"""
Graded Hopf algebras with basis
"""
#*****************************************************************************
#  Copyright (C) 2008      Teresa  Gomez-Diaz (CNRS) <Teresa.Gomez-Diaz@univ-mlv.fr>
#                2008-2011 Nicolas M. Thiery <nthiery at users.sf.net>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#******************************************************************************
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.tensor import tensor
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.with_realizations import WithRealizationsCategory
from sage.misc.cachefunc import cached_method

import six


class GradedHopfAlgebrasWithBasis(GradedModulesCategory):
    """
    The category of graded Hopf algebras with a distinguished basis.

    EXAMPLES::

        sage: C = GradedHopfAlgebrasWithBasis(ZZ); C
        Category of graded hopf algebras with basis over Integer Ring
        sage: C.super_categories()
        [Category of hopf algebras with basis over Integer Ring,
         Category of graded algebras with basis over Integer Ring]

        sage: C is HopfAlgebras(ZZ).WithBasis().Graded()
        True
        sage: C is HopfAlgebras(ZZ).Graded().WithBasis()
        False

    TESTS::

        sage: TestSuite(C).run()
    """

    def example(self):
        """
        TESTS::

            sage: GradedHopfAlgebrasWithBasis(QQ).example()
            An example of a graded connected Hopf algebra with basis over Rational Field

        """
        from sage.categories.examples.graded_connected_hopf_algebras_with_basis import \
            GradedConnectedCombinatorialHopfAlgebraWithPrimitiveGenerator
        return GradedConnectedCombinatorialHopfAlgebraWithPrimitiveGenerator(self.base())

    class WithRealizations(WithRealizationsCategory):
        @cached_method
        def super_categories(self):
            """
            EXAMPLES::

                sage: GradedHopfAlgebrasWithBasis(QQ).WithRealizations().super_categories()
                [Join of Category of hopf algebras over Rational Field
                     and Category of graded algebras over Rational Field]

            TESTS::

                sage: TestSuite(GradedHopfAlgebrasWithBasis(QQ).WithRealizations()).run()

            """
            from sage.categories.graded_hopf_algebras import GradedHopfAlgebras
            R = self.base_category().base_ring()
            return [GradedHopfAlgebras(R)]

    class Connected(CategoryWithAxiom_over_base_ring):
        def example(self):
            """
            TESTS::

                sage: GradedHopfAlgebrasWithBasis(QQ).Connected().example()
                An example of a graded connected Hopf algebra with basis over Rational Field

            """
            from sage.categories.examples.graded_connected_hopf_algebras_with_basis import \
                GradedConnectedCombinatorialHopfAlgebraWithPrimitiveGenerator
            return GradedConnectedCombinatorialHopfAlgebraWithPrimitiveGenerator(self.base())

