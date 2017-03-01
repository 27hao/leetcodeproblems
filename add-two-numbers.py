class Solution(object):

    def addTwoNumbers(self, l1, l2):

        """

        :type l1: ListNode

        :type l2: ListNode

        :rtype: ListNode

        """

        ll1=0

        ll2=0

        i=0

        while l1!=None:

            ll1+=l1.val*(10**i)

            i+=1

            l1=l1.next

        i=0

        while l2!=None:

            ll2+=l2.val*(10**i)

            i+=1

            l2=l2.next

        ll3=ll1+ll2

        result=re=ListNode(0)

        re.next=ListNode(0)

        while ll3>0:

            p=ListNode(ll3%10)

            ll3=ll3/10

            re.next=p

            re=p

        return result.next
