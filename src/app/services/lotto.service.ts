import { DatePipe } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { from, map, tap } from 'rxjs';
import { CASH_FIVE, LOTTO, PICK3, PICK4 } from '../app.constants';

@Injectable({
  providedIn: 'root'
})
export class LottoService {

  constructor(private http: HttpClient) { }

  getCashFiveData() {
    // return this.getData(CASH_FIVE, this.getUrl(CASH_FIVE));
    return this.getLocalData(CASH_FIVE);
  }

  getLottoData() {
    // return this.getData(LOTTO, this.getUrl(LOTTO));
    return this.getLocalData(LOTTO);
  }

  getPick3Data() {
    return this.getLocalData(PICK3);
  }

  getPick4Data() {
    return this.getLocalData(PICK4);
  }

  getLocalData(game: string) {
    return this.http.get(this.getUrl(game));
  }

  getData(game: string, url: string) {
    // return (from(fetch('https://www.texaslottery.com/export/sites/lottery/'+url, { mode: 'no-cors' })) as any)
    return this.http.get(url, { headers: this.getHeaders(), responseType: 'text' })
      .pipe(map(fileText => {
        let rows = (<string>fileText).split(/\r\n|\n/);
        return rows.map(row => {
          const values = row.split(',');
          if (values.length === 0 || values[0] === "") return;
          const numbersArray = this.parseNumbersFromCSVRow(game, values);
          return {
            name: values[0],
            date: this.formatDate(values[3],values[1],values[2], null),
            // pattern: patternCode,
            number: numbersArray.number.join(' '),
            oddCount: numbersArray.number.filter((v: number) => v % 2 === 1).length,
          }
        })
        .filter((data: any) => data && data.name != "").reverse();
      }));
  }

  parseNumbersFromCSVRow(url: string, values: any[]): any {
    let number, ball;
    if (url === 'TWO_STEP') {
      number = [values[4], values[5], values[6], values[7]].map(v => parseInt(v)).sort((a, b) => a - b);
      ball = parseInt(values[8]);
      return {
        number: number.sort((a, b) => a < b ? -1 : 1),
        ball: ball,
        ballIncludedInNumber: number.includes(ball)
      };
    } else if (url === 'ALL_OR_NOTHING') {
      number = [values[4], values[5], values[6], values[7], values[8], values[9], values[10], values[11], values[12], values[13], values[14], values[15]].map(v => parseInt(v)).sort((a, b) => a - b);
      return {
        number: number.sort((a, b) => a < b ? -1 : 1),
      };
    } else if (url === 'MEGA_MILLIONS') {
      number = [values[4], values[5], values[6], values[7], values[8]].map(v => parseInt(v)).sort((a, b) => a - b);
      ball = parseInt(values[9]);
      return {
        number: number.sort((a, b) => a < b ? -1 : 1),
        ball: ball,
        ballIncludedInNumber: number.includes(ball)
      };
    } else if (url === 'POWER_BALL') {
      number = [values[4], values[5], values[6], values[7], values[8]].map(v => parseInt(v)).sort((a, b) => a - b);
      ball = parseInt(values[9]);
      return {
        number: number.sort((a, b) => a < b ? -1 : 1),
        ball: ball,
        ballIncludedInNumber: number.includes(ball)
      };
    } else if (url === 'PICK_4') {
      number = [values[4], values[5], values[6], values[7]].map(v => parseInt(v));
      return {
        number: number,
      };
    } else if (url === CASH_FIVE) {
      number = [values[4], values[5], values[6], values[7], values[8]].map(v => parseInt(v));
      return {
        number: number.sort((a, b) => a < b ? -1 : 1),
      };
    } else if (url === LOTTO) {
      number = [values[4], values[5], values[6], values[7], values[8], values[9]].map(v => parseInt(v));
      return {
        number: number.sort((a, b) => a < b ? -1 : 1),
      };
    }
  }

  filterByDateRange(dateRange: any, data: any) {
    let startDate = dateRange?.startDate;
    if(!startDate) return data; // return all records if start date is null
    let endDate = dateRange?.endDate || new Date(); //by default end date is today
    endDate.setHours(23); // end of the day
    return (data ?? []).filter((item: any) => {
      const d = new Date(item['Date']);
      return d >= startDate && d <= endDate;
    })
  }

  getUrl(game: string) {
    let url = '';
    switch (game) {
      case CASH_FIVE:
        url = url + 'assets/cash_five.json';
        break;
      case LOTTO:
        url = url + 'assets/lotto.json';
        break;
      case PICK4:
        url = url + 'assets/daily4.json';
        break;
      case PICK3:
        url = url + 'assets/pick3.json';
        break;
      default:
        throw Error("Invalid Game Name! " + game);
    }
    return url;
  }

  
  formatDate(year: string, month: string, day: string, eventAt: any) {
    eventAt = eventAt? eventAt : '';
    switch (eventAt) {
      // case Morning:
      //   return new Date(parseInt(year), parseInt(month), parseInt(day))
      default:
        return new Date(parseInt(year), parseInt(month)-1, parseInt(day))
    }
  }

  getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'Accept': 'text/plain',
      'Content-Type': 'text/plain',
      'Access-Control-Allow-Origin': '*'
    });
  }

  getPrettyJson(data: any) {
    return JSON.stringify(data, null, 2)
      // .replace(/ /g, '&nbsp;')
      // .replace(/\n/g, '<br/>');
  }


}
