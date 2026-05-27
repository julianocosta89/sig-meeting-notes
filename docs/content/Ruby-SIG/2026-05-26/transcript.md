SIG: Ruby SIG
Date: 2026-05-26
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/vRdOT8QFjD_J5nUajua1K3WR_tDn58DS4FjvgQm2lI9U0jVqxJTCEIoyJJColKJN.lSe3cmd8jZSDoPrU
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 01:12 And then the horse is turning nice.
So there's a lot of… Alright, let's go ahead and post it.
Which means this is behavioral.
We don't have anything on the agenda today. I wasn't able to make it to the SPECSIG.
dedicated to crafts. But taking a quick look here, looks like there's a new spec release, so that might be out.
Okay, well, we'll take their word for it, even though they seem to be working.
**Arjun Rajappa** 03:04 Okay, Kayla, so… so the voice is a little bit weird, you know, not able to… hear you, hear me.
**Kayla Reopelle** 03:11 Okay, thank you for letting me know. Let me see what I can do.
Let me call you right back, should be about a few minutes. I'll be back in a minute.
**kala** 18:29 Hey! I have been having some internet troubles. I'm sorry for the extended delay. Have you guys been chatting about anything?
Oh no, I can't hear you.
Okay.
Okay, alright, well, I cannot seem to connect to the internet using my computer right now, but, So maybe we can just take this as a more general chatting meeting, and you guys can let me know if there's anything in particular we want to discuss, and I'll just take the notes on my laptop and add them when I can reconnect it to the internet.
Does that sound good?
**Xuan Cao** 19:24 Yeah, sounds great.
**kala** 19:27 Okay, thanks.
So yeah, so what would y'all like to talk about today? Sean, was there anything… I saw that you have a draft PR in declarative config, that's exciting.
Is there anything you wanted to discuss?
**Xuan Cao** 19:41 Yeah, first, so how's, your new repo going? Like, is there a… Coming anytime soon?
**kala** 19:54 Yeah, you know, I haven't heard… we had an issue with, like, teams getting erased and other things that happened last week that kind of lowered it on the agenda. And so now that I think everyone's permissions have been restored, I'll bring up the new repo again. I'm sorry about the delay on that one.
**Xuan Cao** 20:11 Oh, okay, so, okay, got it. Okay, thanks.
Boom.
And, second thing, just the, just, declared configurations, So, I can just briefly talk about this.
So, Basically, I… because I work on… I help my company to, integrate this particular configuration for the goal, so I took a lot of, deep dive for the Go Decker Configuration, I think, the Go approach.
It is, it's very, simple and, very, Effective.
There's also, another very mature decorative configuration implementation, which is from, Java. But, unfortunately, Java, declared configuration took a completely different approach than the goal.
So, because Java has, like, these have, like, a special runtime, And, it can do more, more, automated, say, automated, automated, ticket configuration than, the Go.
The same thing for the Ruby as well. So Ruby is not that, feature, rich than, that… it's not that feature-rich, compared to, Java, but it's similar to Go, so that's the reason I, because I… know the goal, bigger operation, so that's why I implemented the similar, strategy.
And go. So, that's the main reason. And also, I think, I don't know about the other language, because I only took these two languages as a reference.
I don't think JavaScript has this declarative configuration, I don't know about ISON, but I think for other languages, they will follow the goals approach as well, because really, the Java is really a special case, because it's a special runtime.
**kala** 22:27 Okay.
**Xuan Cao** 22:28 Yeah, yeah.
**kala** 22:30 Nice, that's a really helpful background.
**Xuan Cao** 22:33 Yeah, and also, and also, for this, declaration, I chose to create another term.
Which is… people may think it's, like, not necessary, because you can just put it everything that is coded to the same SDK, or even SDK experimental.
as a result, I was thinking quickly, which also follows the same convention as Go. Go have a, like, a dedicated package for this configuration, and that is… doesn't rely on any Dependencies, so it's, like, basically just a code.
File.
And then… If you want to use, Alex component, then you have to… start by yourself, which is, I think, is a more, minimum approach, that it doesn't create a, like, a deep dependency hell, for this kind of a…
**kala** 23:28 Hmm.
**Xuan Cao** 23:29 feature. So, yeah, that's another, another, another, implementation strategy I choose, not dependent on any, external dependency.
**kala** 23:43 Okay, nice.
**Xuan Cao** 23:45 And, and then finally, I separate this, so currently I only have, like, one, component, which is, the choice provider. So I wanted to, define the general approach to take some ideas and then feedback to say, is this a good approach, or is this, some, something we need to improve, or we need a… Different to take another bit… you know.
Think it, think, yeah, think it differently. So… Gongs.
And at least on, it will be our meter provider and the local providers. I'm not sure if you are willing to contribute on the local providers.
**kala** 24:29 Yeah, I can contribute on the logger providers if you'd like me to.
**Xuan Cao** 24:34 Okay, okay. No, that's, that's, that's… yeah, that's everything I wanted to discuss about this, PR. and then just to, about the the current feedback from the, GEMS.
I'll reply, but I just, just want to be, heads up that the current, The current approach is very minimal, There's a… it kind of doesn't take, customized, components.
He only… He only considered… what it currently has inside the SDK.
So… so, I mean, we can do a lawsuit into To enable the customization, or, like, But that will just make the PR so big to review.
**kala** 25:33 Yeah.
**Xuan Cao** 25:33 That's why I actually separated, like, into 3 different components, like base paradder, meter paradeter, low paradeter. So… I mean, using AI, I can create all of them together, but I don't think that's a very good thing for the reviewer.
**kala** 25:50 Yeah, yeah, I… I hadn't seen his comments yet, but just for me personally to review, I think that I saw that there was, like, 27 files. I feel like that's… that's a good number for a review, and I'd rather… know that declarative configuration works with the configurations that we have before we add new features to bring in other types of config and wider options. So I'm in alignment with you there.
**Xuan Cao** 26:18 Okay, okay, thanks. I'll… I'll, I'll respond to his, review, and then,
**kala** 26:23 Okay.
**Xuan Cao** 26:25 And we can start working from there.
**kala** 26:28 Okay, great.
Thank you. Thank you for thinking through this, and I'm glad that your experience with Go can help with the Ruby implementation.
Cool. Alright, so… Arjun, was there anything that you wanted to cover today?
**Arjun Rajappa** 26:53 Nothing specific, though, there were a few PRs which are trending.
The PR relationship to… Hotels, we actually see common, as well as… Sitting the exporter into 3 different groups.
**kala** 27:11 The three different PRs about exporters.
**Arjun Rajappa** 27:14 Yeah.
**kala** 27:15 Okay.
Yes.
I saw that you made some… sorry, it's… my audio is not working great again. I saw that you made… Some changes to them, is there anything, Sync, that you wanted to go over?
**Arjun Rajappa** 27:34 Nothing? Nothing specific?
**kala** 27:37 Okay.
Sounds good. Well, yeah, well, thank you, thank you for… for updating those, and I can take a look at them again.
Alright, let's see… Is there anything else done?
That, you noticed or want to talk about together today? Anyone here?
All right, well, thank you very much for your patience with my weird internet situation this morning. I'm not exactly sure what's going on. But, yeah, I'm glad you… you hung on the call, and that we got a chance to chat a bit.
So, have a… have a nice week then, and I guess I'll talk to you all next week around Slack.
**Xuan Cao** 28:51 It's true.
Thanks.
**Arjun Rajappa** 28:53 They…
