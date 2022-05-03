import React from "react";
import { Box, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    justifyContent: "space-between",
    marginLeft: 20,
    flexGrow: 1,
  },
  username: {
    fontWeight: "bold",
    letterSpacing: -0.2,
  },
  previewText: {
    fontSize: 12,
    color: "#9CADC8",
    letterSpacing: -0.17,
  },
  previewTextUnread: {
    fontSize: 14,
    fontWeight: "bold",
    color: "#000000",
    letterSpacing: -0.17,
  },
  unreadCountContainer: {
    marginLeft: 10,
    marginRight: 10,
    background: "rgb(63,146,255)",
    color: "#ffffff",
    minWidth: 24,
    height: 24,
    alignSelf: "center",
    borderRadius: 12,
  },
  unreadCount: {
    fontSize: 16,
    paddingLeft: 6,
    paddingRight: 6,
    textAlign: "center",
  }
}));

const ChatContent = ({ conversation }) => {
  const classes = useStyles();

  const { otherUser } = conversation;
  const latestMessageText = conversation.id && conversation.latestMessageText;

  return (
    <Box className={classes.root}>
      <Box>
        <Typography className={classes.username}>
          {otherUser.username}
        </Typography>
        <Typography className={conversation.unreadCount ? classes.previewTextUnread : classes.previewText}>
          {latestMessageText}
        </Typography>
      </Box>
      {conversation.unreadCount ? 
      <Box className={classes.unreadCountContainer}>
        <Typography className={classes.unreadCount}>
          {conversation.unreadCount}
        </Typography>
      </Box>
      : <></>}
    </Box>
  );
};

export default ChatContent;
