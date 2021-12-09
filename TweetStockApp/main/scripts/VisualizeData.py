import yfinance as yf
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.figure_factory as ff
from datetime import datetime, timedelta
import json
import os


class Visualize():

    def generate_stock_data(self, ticker, start_date_obj):
        # print("param: start: " + str(start_date_obj))
        # print("param: today: " + str(datetime.today().strftime('%Y-%m-%d')))

        if(start_date_obj != str(datetime.today().strftime('%Y-%m-%d')) and start_date_obj.weekday() < 4):
            day_check = datetime.today() - start_date_obj
            if(day_check.days > 30):
                interval = '1h'
            else:
                interval = '1m'
            end_date_obj = start_date_obj + timedelta(days=1)
            start_date = datetime.strftime(start_date_obj, '%Y-%m-%d')
            end_date = datetime.strftime(end_date_obj, '%Y-%m-%d')
            print("start_date: " + start_date)
            print("end_date: " + end_date)
            data = yf.download(tickers=ticker, start=start_date,
                               end=end_date, period='$d', interval=interval)
        else:
            data = yf.download(tickers=ticker, period='$d', interval='1m')
        return data

    def generate_graph(self, ticker, data):
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=data.index, y=data['Open'], name='Open'))
        fig.add_trace(go.Scatter(
            x=data.index, y=data['Close'], name='Close'))
        fig.layout.update(title_text=("Time Series Data: " +
                                      ticker), xaxis_rangeslider_visible=True)
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m",
                         step='minute', stepmode="backward"),
                    dict(count=45, label="45m",
                         step='minute', stepmode="backward"),
                    dict(count=3, label="3h", step='hour',
                         stepmode="backward"),
                ])
            )
        )
        fig.update_yaxes(title_text=(
            str(ticker) + " Close Price"), tickprefix='$')

        plt_div = plot(fig, output_type='div', auto_open=False,
                       show_link=False, config=dict(displayModeBar=False))

        return plt_div

    def generate_json_records(self, df):
        json_records = df.reset_index().to_json(orient='records')
        # json.loads(json_records) -> python dictionary
        # json.dumps(json.loads(json_records), indent=4) -> json formt
        data = json.loads(json_records)
        return data
