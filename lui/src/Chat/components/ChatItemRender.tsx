import React, { type FC } from 'react';
import '../index.css';

interface IProps {
  direction: 'start' | 'end';
  avatar?: React.ReactNode;
  title: React.ReactNode;
  content: React.ReactNode;
  starter?: React.ReactNode;
}

const ChatItemRender: FC<IProps> = ({
  direction,
  avatar,
  title,
  content,
  starter = <></>,
}) => {
  return (
    <>
      <div
        className={`flex ${
          direction === 'start'
            ? 'flex-row ant-pro-chat-list-item-left'
            : 'flex-row-reverse ant-pro-chat-list-item-right'
        } ant-pro-chat-list-item ant-pro-chat-list-item-message-content gap-[12px] p-[16px] chat_item_container`}
      >
        {avatar}
        <div className="ant-pro-chat-list-item-message-container">
          {title}
          {content}
        </div>
      </div>
      {starter}
    </>
  );
};

export default ChatItemRender;
