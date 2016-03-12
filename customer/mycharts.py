import sys

from reportlab.lib.colors import PCMYKColor, red, Color, CMYKColor, yellow
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, String
from reportlab.pdfbase.pdfmetrics import stringWidth, EmbeddedType1Face, registerTypeFace, Font, registerFont
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.validators import Auto
from workorder.models import WorkOrder

class Bar(_DrawingEditorMixin,Drawing):
    def __init__(self,date_to, date_from, width=1175,height=575, *args,**keywords):
        apply(Drawing.__init__,(self,width,height)+args,keywords)
        
        from_month = int(date_from[6])
        to_month = int(date_to[6])

        list_of_months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        # font 
        fontName = 'Times-Roman'
        # chart
        self._add(self,VerticalBarChart(),name='chart',validate=None,desc=None)
        self.chart.width = 1175
        self.chart.height = 575
        self.chart.x = 50
        self.chart.y = 50 
        # colors
        self._colors = (PCMYKColor(100, 67, 0, 23), PCMYKColor(60, 40, 0, 13), PCMYKColor(100,0,46,46), PCMYKColor(70,0,36,36))
        # chart bars
        self.chart.bars.strokeColor = None
        self.chart.bars.strokeWidth = 0
        # we have four series here
        for i, color in enumerate(self._colors): self.chart.bars[i].fillColor = color
        self.chart.barSpacing = 4
        self.chart.barWidth = 14
        self.chart.barLabelFormat   = '%s'
        self.chart.barLabels.nudge           = 5
        self.chart.barLabels.angle           = 90
        self.chart.barLabels.fontName        = fontName
        self.chart.barLabels.fontSize        = 10
        # categoy axis
        self.chart.categoryAxis.categoryNames = []
        self.chart.categoryAxis.labelAxisMode='low'
        self.chart.categoryAxis.labels.angle = 0
        self.chart.categoryAxis.labels.boxAnchor = 'n'
        self.chart.categoryAxis.labels.dy = -6
        self.chart.categoryAxis.labels.fillColor = PCMYKColor(0,0,0,100)
        self.chart.categoryAxis.labels.fontName = fontName
        self.chart.categoryAxis.labels.fontSize = 14
        self.chart.categoryAxis.labels.textAnchor='middle'
        self.chart.categoryAxis.tickShift=1
        self.chart.categoryAxis.visibleTicks = 0
        self.chart.categoryAxis.strokeWidth     = 0
        self.chart.categoryAxis.strokeColor         = None
        # sample data
        
        workorders = WorkOrder.objects.filter(date_created__gte=date_from, date_created__lte=date_to)
        count      = workorders.count()
        
        sales      = [0,0,0,0,0,0,0,0]
        
        net_sales  = [0,0,0,0,0,0,0,0]
        
        sales_goal = [9000, 8000, 9200, 10200, 16000, 20000, 22000, 20000, 20000, 16000, 11000, 6000]
        i = 0
                

        

        for j in range(from_month-1,to_month ):
            self.chart.categoryAxis.categoryNames.append(list_of_months[j])
            

        for workorder in workorders:
            sales[i] += workorder.estimate_revision
            net_sales[i] += workorder.estimate_revision - sales[i]*.34
            i = i + 1
                

        # The first number in the set is the bar value.
        self.chart.data = [(sales[0], sales[1], sales[2], sales[3], sales[4], sales[5], sales[6], sales[7]), 
                           (sales_goal[0], sales_goal[1], sales_goal[2], sales_goal[3], sales_goal[4], sales_goal[5], sales_goal[6], sales_goal[7]),
                           (net_sales[0], net_sales[1], net_sales[2], net_sales[3], net_sales[4], net_sales[5], net_sales[6], net_sales[7])]
        self.chart.groupSpacing = 15
        # value axis
        self.chart.valueAxis.avoidBoundFrac     = None
        self.chart.valueAxis.gridStrokeWidth    = 0.25
        self.chart.valueAxis.labels.fontName    = fontName
        self.chart.valueAxis.labels.fontSize    = 16
        self.chart.valueAxis.rangeRound         = 'both'
        self.chart.valueAxis.strokeWidth        = 0
        self.chart.valueAxis.visibleGrid        = 1
        self.chart.valueAxis.visibleTicks       = 0
        self.chart.valueAxis.visibleAxis        = 0
        self.chart.valueAxis.gridStrokeColor    = PCMYKColor(70,0,36,36)
        self.chart.valueAxis.gridStrokeWidth    = 0.25
        self.chart.valueAxis.valueStep          = None#3
        self.chart.valueAxis.labels.dx          = -3
        # legend
        self._add(self,Legend(),name='legend',validate=None,desc=None)
        self.legend.alignment = 'right'
        self.legend.autoXPadding = 6
        self.legend.boxAnchor = 'sw'
        # series
        self._seriesNames = 'Gross Sales', 'Expected Sales', '', 'Net Sales'
        #self.legend.colorNamePairs = [(constants.COLOR_1, 'MSILF Treasury Institutional'), (constants.COLOR_2, 'Lipper Institutional U.S. Treasury Money Market Average')]
        self.legend.columnMaximum = 3
        self.legend.dx = 8
        self.legend.dxTextSpace = 4
        self.legend.dy = 6
        self.legend.fontSize = 14
        self.legend.fontName = fontName
        self.legend.strokeColor = None
        self.legend.strokeWidth = 0
        self.legend.subCols.minWidth = 55
        self.legend.variColumn = 1
        self.legend.x = 10
        self.legend.y = -25
        self.legend.deltay = 10
        # x label
        self._add(self,Label(),name ='XLabel',validate=None,desc="The label on the horizontal axis")
        self.XLabel._text = ""
        self.XLabel.fontSize = 6
        self.XLabel.height = 0
        self.XLabel.maxWidth = 100
        self.XLabel.textAnchor ='middle'
        self.XLabel.x = 140
        self.XLabel.y = 10
        # y label
        self._add(self,Label(),name='YLabel',validate=None,desc="The label on the vertical axis")
        self.YLabel._text = ""
        self.YLabel.angle = 90
        self.YLabel.fontSize = 6
        self.YLabel.height = 0
        self.YLabel.maxWidth = 100
        self.YLabel.textAnchor ='middle'
        self.YLabel.x = 12
        self.YLabel.y = 80
        self.legend.autoXPadding     = 65

    def getContents(self):
        self.legend.colorNamePairs = zip(self._colors, self._seriesNames) 
        return apply(Drawing.getContents,(self,))

    def debug_print(self, msg):
        print >>sys.stderr, msg

if __name__=="__main__": #NORUNTESTS
    test = dict()
    test = {
        'a' : 'b'
    }
    BarChart01(**test).save(formats=['pdf'],outDir='static/pictures/',fnRoot=None)