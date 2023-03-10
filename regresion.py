import matplotlib.pyplot as plt
import pandas.plotting as pd_plot
import numpy as np
import pandas as pd
import seaborn as sns

class regresion:
    def hola (self):
        print("hola")
        
    def histogramas(self,df):
        sns.displot(df.iloc[:,0])
        sns.displot(df.iloc[:,1])
        sns.displot(df.iloc[:,2])
        sns.displot(df.iloc[:,3])
        sns.displot(df.iloc[:,4])
        sns.displot(df.iloc[:,5])
        pass
    
    def dispersion(self,df80):
        fig,ax = plt.subplots()
        corr_matrix = df80.corr()
        ax.scatter(corr_matrix.Salesprice, corr_matrix['Overall Quality'], s=50, c='blue', alpha=0.5)
        plt.show()
        ax.set_xlabel('Overall Qualilty')
        ax.set_ylabel('Sales Price')
        ax.set_title('Sales price vs Overall Quality')
        pd_plot.scatter_matrix(df80, figsize=(20, 20))
        plt.show()
        # Crear los histogramas
        fig, axs = plt.subplots(len(df80.columns), len(df80.columns), figsize=(25, 25))  
        # Crear ciclo for 
        for i in range(len(df80.columns)):     
            for j in range(len(df80.columns)):         
                # Graficos de dispersion e histogramas
                        axs[i,j].scatter(df80[df80.columns[j]], df80[df80.columns[i]], alpha=0.5)         
                        axs[i,j].xaxis.set_tick_params(labelbottom=False)         
                        axs[i,j].yaxis.set_tick_params(labelleft=False)  
                # Correlacion calculada
                        corrcoef = df80[df80.columns[j]].corr(df80[df80.columns[i]])
                        axs[i,j].text(0.05, 0.95, f"Corr: {corrcoef:.2f}", transform=axs[i,j].transAxes,ha="left", va="top") 
                        # Etiquetas en columnas         
                        if i == len(df80.columns)-1:             
                            axs[i,j].set_xlabel(df80.columns[j])         
                            if j == 0:             
                                axs[i,j].set_ylabel(df80.columns[i])         
                                if i == 0 and j == 0:             
                                    axs[i,j].set_title(df80.columns[j]) 
                                            # Ejes ajustados         
                                x_desc = df80[df80.columns[j]].describe()
                                y_desc = df80[df80.columns[i]].describe()
                                x_min, x_max = x_desc['min'], x_desc['max']
                                y_min, y_max = y_desc['min'], y_desc['max']
                                x_margin, y_margin = (x_max-x_min)*0.1, (y_max-y_min)*0.1
                                axs[i,j].set_xlim(x_min-x_margin, x_max+x_margin)
                                axs[i,j].set_ylim(y_min-y_margin, y_max+y_margin)
        
                    
        return plt.show()
    def separacion(self,df,separacion = 0.8):
        df80 = df.iloc [0:int(separacion*len(df)),0:5]
        df20 = df.iloc [int(separacion*len(df)):len(df),0:5]
        return df80,df20
        
    def modeloml(self,df80,b0 =0.02,b1 =0.01,epochs = 100, learning_rate=0.001):
        x = df80["Overall Quality"].values
        y = df80["Salesprice"].values
        error_df = pd.DataFrame (columns=["Epoch", "Error",'b0','b1'])
        x =pd.DataFrame(x)
        ones = np.ones((x.shape[0], 1))
        ones= pd.DataFrame(ones)
        x = np.hstack((x,ones))
        x = pd.DataFrame(x)
        print(x.values)
        for i in range (epochs):
            prediccion = np.dot(x.values,[b1,b0])
            error = prediccion-y
            error_medio =np.divide(np.sum(np.power(error,2)),np.multiply(2,len(error))) 
            b0 = b0-learning_rate*np.divide(np.sum(error*df80["Overall Quality"].values),len(error))
            b1 = b1-learning_rate*np.divide(np.sum(error),len(error))
            error_df = pd.concat([error_df, pd.DataFrame({"Epoch": [i], "Error": (error ** 2).mean()/2 ,'b0':b0,'b1':b1 })])
            print(i,error_medio)
        return(error_df)   
    
    def mode (self,modelo):
        modelo.plot(x="Epoch", y="Error",color='red')
        plt.xlabel("Epoch")
        plt.ylabel("Error")
        m=7
        print(4071.106782+29204.812826*m)
        modelo.to_csv("Modelo.csv",index=False)
        Parametros = modelo.iloc[-1].to_dict()
        Parametros
        Parametros["b0"] 
        pass