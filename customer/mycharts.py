#    mycharts.py  
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from customer.models import Customer
from workorder.models import WorkOrder
from django.utils import timezone

class MyBarChartDrawing(Drawing):
    def __init__(self, width=1000, height=400, *args, **kw):
        
        Drawing.__init__(self,width,height,*args,**kw)
        self.add(HorizontalBarChart(), name='chart')

        self.add(String(480,380,'Work Order Total Costs'), name='title')

        #set any shapes, fonts, colors you want here.  We'll just
        #set a title font and place the chart within the drawing
        self.chart.x = 50
        self.chart.y = 20
        self.chart.width = self.width - 10
        self.chart.height = self.height - 40

        self.title.fontName = 'Helvetica-Bold'
        self.title.fontSize = 16
        
        work_orders = WorkOrder.objects.all()
        count = WorkOrder.objects.count()
        
        data_list = list()

        for work_order in work_orders:
            data_list.append(work_order.estimate_revision)

        self.chart.data = [data_list]

if __name__=='__main__':
    #use the standard 'save' method to save barchart.gif, barchart.pdf etc
    #for quick feedback while working.
    MyBarChartDrawing().save(formats=['gif','png','jpg','pdf'],outDir='.',fnRoot='barchart')