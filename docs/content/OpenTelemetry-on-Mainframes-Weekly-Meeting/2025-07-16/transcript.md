SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-07-16
Duration: 6 minutes
Zoom Recording URL: https://zoom.us/rec/share/3lZruRYx9V2QEGngohqBN7ygnhGxFkKILEEN5tss7vOxWusAdkfTF4SbNtKCfAUw.W6GjWhnxAWuHEZyl
============================================================

## Zoom Recording Transcript

**Anand Somasundaram** 00:12 Hey, Greg!
**Greg Shriver** 00:14 Hey, Anand, how are you?
**Anand Somasundaram** 00:16 I'm doing well, how about you?
**Greg Shriver** 00:17 Good, good, good.
**Anand Somasundaram** 00:19 I'm not sure anybody is going to join today.
**Greg Shriver** 00:22 I don't know, either. I mean, one of the reasons I joined was.
you know, because we changed the time.
I just if somebody new joins wanted to. Wanted to be here to welcome them, I guess, and but I don't have anything.
I mean, I don't have any any like new agenda items.
and Jim already updated the notes.
**Anand Somasundaram** 00:50 And Rodica posted a slack message especially for you, I think.
Yeah, he said. He said he couldn't make it this week.
Yeah.
**Greg Shriver** 00:59 Yeah, he's traveling so but he did. He did provide some notes.
He says he's yeah. Let me. I'll just share my screen.
No, I don't want to share the screen I want to share.
I want to share.
Oh, that's right here.
So can you see my screen.
**Anand Somasundaram** 01:25 Yeah, I can.
**Greg Shriver** 01:26 So. Yeah, he he said that he was still working on the the Survey. Blog the draft for the Survey blog. So I wasn't sure. I mean, I know, he said, we would post a spreadsheet to help our discussion on the semantic conventions for metrics. I I wonder if that maybe was a follow on to the conversation we had about the different process models last week.
and so so that, looking forward to that this 3rd comment from him. I don't know exactly what that means.
so I guess he attended the semantic convention, Sig.
And.
**Anand Somasundaram** 02:10 I think that this came from Morgan. I believe.
**Greg Shriver** 02:13 Oh, it did!
**Anand Somasundaram** 02:14 Yeah, more. If you look at the slack message. Morgan posted something
**Greg Shriver** 02:20 Oh, I did not see that. Okay.
**Anand Somasundaram** 02:28 Oh, maybe not sorry. I'm.
**Greg Shriver** 02:30 Yeah.
**Anand Somasundaram** 02:30 I misspoke.
**Greg Shriver** 02:33 So yeah, I haven't seen Morgan, but so maybe maybe Rudiga maybe Rudiga attended this. The semantic convention. Sig, I'm not sure I I wasn't aware that they even that they needed a prototype implementation to you know, to approve the Prs. I that's first.st I've heard of it, so we'll probably have to get, you know, more, more information from from Rudiga when he shows up.
**Anand Somasundaram** 03:02 Yeah.
**Greg Shriver** 03:03 Next week.
**Anand Somasundaram** 03:03 I I agree.
**Greg Shriver** 03:05 You know.
**Anand Somasundaram** 03:06 It's going to be a little dicey right? Who's going to do the prototype?
**Greg Shriver** 03:10 Oh, yeah, yeah, yeah. Well, and and maybe maybe that's something that we can all collaborate on. I mean.
well, we'll see.
Yeah.
So I mean other than that I don't have anything new for this week. Do you have anything.
**Anand Somasundaram** 03:29 No, I don't have anything else.
**Greg Shriver** 03:31 Okay.
**Anand Somasundaram** 03:32 Once Rodriga comes in. Probably I need to get more hands on and involved in some of this, because I have a a lot of prism experience.
**Greg Shriver** 03:42 Yeah.
**Anand Somasundaram** 03:43 So I'll jump in and provide some value.
**Greg Shriver** 03:47 Yeah, for sure. I mean, yeah, yeah, this is, this is all good. So so well, so we're 5 min in. I I don't know. Do you wanna call it a wrap for this week?
**Anand Somasundaram** 04:01 Yeah. Sure. Are you? A long time, broadcom?
**Greg Shriver** 04:05 I am. I've been well, I've been with the combined. I started out with Legion.
So that was a long, long time ago, back in 94, and then Legion became Ca.
and then Ca, became broadcom.
So I've been. I've been here since 94. So a long time, long time.
**Anand Somasundaram** 04:29 I used to work in broadcom.
**Greg Shriver** 04:32 Oh, you did!
**Anand Somasundaram** 04:33 Hyderabad, for between 2,010 and 12.
**Greg Shriver** 04:37 Oh, okay.
**Anand Somasundaram** 04:38 Jim Broaddust, Jordan Heise.
**Greg Shriver** 04:42 Yeah, yeah, I remember, Jordan, yeah.
**Anand Somasundaram** 04:45 Yeah, I think he's still there, right?
**Greg Shriver** 04:48 I think so. He's in the data.
dB, 2 tools. Yeah, he's in a different value stream. So we they have us all split up on, you know, in value streams.
**Anand Somasundaram** 04:58 Oh, okay.
**Greg Shriver** 04:59 So, yeah, yeah, so I don't. I haven't talked to Jordan in a while. I mean when you know. But yeah, but yeah, yeah.
**Anand Somasundaram** 05:09 But yeah, so how were you?
**Greg Shriver** 05:11 Oh, for sure, for sure!
And what did you do?
**Anand Somasundaram** 05:16 I was a senior architect working on the dB. 2 tools to modernize those dB, 2 tool set right. It was from the Rcq. Rcms. Of the world.
**Greg Shriver** 05:30 Yeah.
**Anand Somasundaram** 05:31 C plus plus.
**Greg Shriver** 05:32 Oh, wow! Wow!
**Anand Somasundaram** 05:33 I did.
**Greg Shriver** 05:34 And what are you doing? And and you're with Ibm. Now.
**Anand Somasundaram** 05:37 Yeah, I 2,012. I came back to Ibm. I was in Ibm.
**Greg Shriver** 05:42 Oh, you were an Ibm, and you came to Broadcom, or well, Ca, at the time, I guess.
**Anand Somasundaram** 05:47 Yeah, yeah.
**Greg Shriver** 05:48 And then came back, oh, okay, alright. And what are you doing for? For Ibm.
**Anand Somasundaram** 05:53 I work on this. I'm the architect for Zapm connect.
**Greg Shriver** 05:56 Zapm, connect? Oh, okay. Yeah. Yeah. Yeah.
**Anand Somasundaram** 05:59 Yeah, that's the Apm tool monitoring the transactions.
**Greg Shriver** 06:04 Yeah, I'm quite familiar with it. Yeah.
Oh, okay, that's all awesome. Yeah. Yeah.
Well, you're in the right place. Yeah.
**Anand Somasundaram** 06:12 Yeah.
Okay. Then, nice talking to you.
**Greg Shriver** 06:16 Yeah, good talking to you, too. Anand I guess we'll see you next week.
**Anand Somasundaram** 06:21 Okay, talk to you bye.
**Greg Shriver** 06:22 All right. See you. Bye-bye.
