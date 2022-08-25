import { useState, useEffect, useRef } from 'react';
import styles from "./Modals.module.scss";


export default function useModal() {

  const [active, setActive] = useState(false)
  const cardRef = useRef();

  useEffect(() => {
    const handleClick = (event) => {
      if (cardRef.current && !cardRef.current.contains(event.target)) {
        setActive(false)
      }
    };
    document.addEventListener('click', handleClick, true);
    return () => {
      document.removeEventListener('click', handleClick, true);
    };
  }, [cardRef]);



  const ModalComponent = () => {
    return (
      <div className={styles.modalbg} >
        <div className={styles.card} ref={cardRef} >
          <div className={styles.header} >
            header
            <button onClick={() => setActive(false)}>boton cerrarme</button>
          </div>
          <div className={styles.body} >
            body
          </div>
          <div className={styles.footer} >
            footer
          </div>
        </div>
      </div>
    )
  }
  return { ModalComponent, active, setActive }
}
