SIG: Python SIG
Date: 2025-10-30
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:04 Hello.
**Madaket Beach (us-cam-5cc)** 01:08 alone.
**Tammy Baylis** 01:11 Hey, welcome back, Ricardo.
**Marcelo Trylesinski** 01:15 Nope.
**Riccardo Magliocchetti** 02:23 So, welcome, everyone, to this week's Python Seek Call.
And… we'll wait.
A few more minutes for more people to join.
In the meantime, please add yourself to the attendee list in the notes, and I'm sharing the link in the chat.
And also, if you have any last-minute topic, please add it. Thanks.
Okay, we have 5 minutes in, I think we can start.
Again, welcome again.
And… Yeah, the first topic?
I think it's from… Someone from Microsoft?
About log breaking changes?
Anyone have a clue?
Or want to discuss this.
**Tammy Baylis** 04:58 I think this was, Hector's from last week, and it seems he won't be able to join this time.
**Riccardo Magliocchetti** 05:08 Okay.
Okay, well, we can discuss it anyway. So, log-breaking changes and release plan. Every year, we have release freeze starting mid-November in Microsoft.
So it would be great to have some plans for this soon.
And… well, I can just say that I'm back from a week vacation.
Yeah. We discussed it.
two meetings ago, but we'll try to merge, I think, four… 6… 7, 6… PR first.
Yeah, like, hopefully we can gather these out.
In two weeks.
And so, in order to do so.
help in reviewing these two PRs.
46764647 is really appreciated.
Anyone else?
**Madaket Beach (us-cam-5cc)** 06:49 I think… were we gonna discuss this with, some… Like, external users of the logs, right?
Didn't we open an issue on someone's GitHub?
**Riccardo Magliocchetti** 07:10 I don't think so, but… I… Like, we get a niche, we got an issue.
From someone that was seeing the… The warning… let me check… And also, I pinged the Pydante people.
That's at least a couple of… Of certain users are aware of the changes?
Okay.
We got this one.
Yeah.
**Madaket Beach (us-cam-5cc)** 08:00 Yeah, that's a valid complaint, I think.
But hopefully that'll be fixed next release.
**Riccardo Magliocchetti** 08:09 Yep.
**Aaron Abbott** 08:13 I think Alex left a similar… like, question and slide, Alex from Pydentic.
But, if I remember right, this will only show up for people who are using these.
Sorry, they should only be showing up for people who are using log record, Oh, I see, I see.
Nevermind. I got it.
**Riccardo Magliocchetti** 08:54 So… Yeah, so, like, like, my… like, what I would prefer to do is, like, to get visa release out as soon as possible, and try to fix… Whatever we need to fix after that, right?
Otherwise, like, we won't, move these logs, forward anytime.
Okay, another top, comment?
Otherwise, we move to the next topic.
From… Kyiv?
PR for review, additional some co-artibus in JAOTs.
**Keith Decker** 09:53 Yep, got some reviews on that yesterday, I think you guys who did that. There is a comment in there I'd like to talk about with the group, Down there… that one you just scrolled past, sorry.
from Lumella, and Dylan responded, too, about Lumila mentioned that if we get no response from an LLM, we should change the finish region to error, and Dylan had a good point.
follow up there that I'm also on the same boat, but I wanted to talk with everybody else and see what their thoughts are.
**Marcelo Trylesinski** 10:34 Wh-wh-why is a… Why would the Finnish reason be set to error?
**Keith Decker** 10:40 According to that comment in another SEMCOMF… Issue.
It should… they… they were in there talking about if finished reasons are missing, it should be air, and I… I don't know any of the history around that, but I don't… I don't think that I should be dictating if it's an error, for finish reasons.
are empty, that's something I think the instrumentation should be handling.
**Aaron Abbott** 11:06 I think we had a discussion on this in the Gen AI SIG, and Dylan, you raised, like, a valid question.
Which was, like.
how does this util detect if there's error? Like, what do we do in the case of error in the… in, like, the… The span, should we still created, et cetera, et cetera.
And one of the things, I guess, Lamilla raised was, if you don't have a… you wouldn't have a finish reason if the request failed, right? So I think… the idea here is that if it's none, you assume it's an error, but I do… Yeah, Dylan, your point makes sense to me, also.
**Madaket Beach (us-cam-5cc)** 11:45 Ian, do you have any code for… Do you have, like, an on-error method or something?
**Keith Decker** 11:52 Yeah, there is a fail LLM method in the Hounder that we would expect the instrumentation to use if they detect an error, or whatever, right?
This was just some defensive programming around… a finish, if finish reasons was empty, I don't set the span attribute right, because it's not allowed to be none, so it just doesn't get set.
**Madaket Beach (us-cam-5cc)** 12:27 Yeah, I think that… The way you have it now is fine.
Yeah, I… there's maybe another discussion around when Should you not set the attribute at all?
And I think, like, the way you do now, you say, if the… What gets passed in is not none. Then you set the attribute.
**Keith Decker** 12:53 Right.
**Madaket Beach (us-cam-5cc)** 12:54 And I think that's good, because then you can pass in, like.
Zero, or, like, empty list, or something, and the attribute still gets set.
Because I think there are cases where you still want to set the attribute to, like, a default value.
That was another discussion we were having, is like.
when it's a default value, is it better to not set it at all, or to set it with, like, with a default value? I don't know if anyone has thoughts on that.
**Marcelo Trylesinski** 13:33 Are we storing in a dictionary?
**Keith Decker** 13:41 I'm sorry, I wasn't.
**Marcelo Trylesinski** 13:42 Are we storing all the data in a dictionary, or is it a data class?
**Keith Decker** 13:47 It's a dictionary on a data class for that one.
**Marcelo Trylesinski** 13:51 retaliatory?
**Keith Decker** 13:52 It's a dictionary on a data class.
On that one.
So, the attribute is actually, yes, a dictionary, but there is, I'm trying to remember if that one has… enums that it runs through or not. Let me go look.
**Madaket Beach (us-cam-5cc)** 14:11 I mean, it's… it's a data class, right? There's, like, an LLM invocation data class.
that we…
**Keith Decker** 14:18 Okay, so finish reasons are a list of strings.
**Marcelo Trylesinski** 14:25 Yeah, but what's these attributes?
The dictionary.
**Keith Decker** 14:29 Yes. And some confidence.
**Madaket Beach (us-cam-5cc)** 14:32 Yeah.
**Marcelo Trylesinski** 14:35 I mean, I usually have a preference to not include what's not needed.
For tactics.
If at some point we want to improve the typing of this whole thing, instead of using date, string to… Any, then we can use not required.
Spent off having… Non-fields.
**Aaron Abbott** 15:07 Is… is this code not typed, though? I thought.
**Marcelo Trylesinski** 15:12 Well, you have levels of strictness.
But this is, this is okay.
**Aaron Abbott** 15:18 So, Keith, like, this finish reasons, this is a list of string, right?
**Keith Decker** 15:23 Yeah, it's a list of strings.
**Aaron Abbott** 15:25 And it's not something we had to cast or check, it's just part of the data class that gets passed in, right?
**Keith Decker** 15:30 Yes.
**Marcelo Trylesinski** 15:31 Alright, what I meant is, if you go to, search for attributes column, please, Ricardo.
Yeah, this one. 137. No… That's, that's good, no? That's also good. Yeah, so this one. You know already which are the attributes, right? So you can… Populated that.
Like, here is a dictionary of string any, but you actually know what's the shape of the string… of the.
**Keith Decker** 16:04 Right, so this is running through… the LLM invocation and just grabbing valid attributes that need to be set to a span. This isn't actually set on the… the… the typed LLM invocation, this is just translation from the LLM invocation to the span attributes. So it runs through each of the… each of the, yeah, attributes on the LM invocation, and then is making a dictionary that's just using the span setAttribute function to to put them on there. So it's cleaning up ones that are none… Or… whatever there. It's just a temporary.
Holding.
But the actual finish reasons on the LLM indication is a typed-of list of strings.
**Aaron Abbott** 17:12 Marcel, maybe if you have a chance, would you mind just leaving a comment here, if that doesn't… Address your concern.
**Marcelo Trylesinski** 17:20 Ehh… I mean, based on this, it's just, What's written in the, in the… In the specification. Do we set values?
Or we prefer to not set values.
**Keith Decker** 17:39 So, when I've been going through building this, I've been preferring to not set values because the… Attributes don't like being set to none if there were no.
Because a lot of other attribute values need a value filled for it, so it doesn't like none, so I've just been excluding the attribute if If it's not supplied to me.
I don't know if that's how Semcoms reverse it or not.
But I can't set none for a lot of them, so I would have to do, what, an empty value if we want to?
Keep the attribute on the span?
**Marcelo Trylesinski** 18:18 I think you're doing the right thing.
**Keith Decker** 18:21 Okay.
**Riccardo Magliocchetti** 18:25 I also think this matches what other instrumentation are doing.
But this, if it is not none.
Just set it, otherwise just keep it.
So…
**Keith Decker** 18:38 Okay, so to the original comment, then.
GenAI utils shouldn't be inferring that an empty finish reason is an error, right? We should just let the instrumentation deal with what they actually set as an error or not.
Is that the consensus I'm getting here?
**Aaron Abbott** 18:59 It sounds like we're talking about two different issues, right?
**Keith Decker** 19:01 Yeah, I think we kind of deviated from… the original into… Setting attributes or not.
**Aaron Abbott** 19:09 So yeah, on the one hand, I guess it's a general question of, like, if you… If you don't have a value to set on a… if you don't have the value for an attribute, do you set it with some kind of zero empty value, or do you alight it from the attributes? That's the one question, and then the other one was specifically about inferring error from finish reasons, right?
**Keith Decker** 19:30 Right. Yeah, those are the two issues.
I think we answered the first one in that.
don't fill, or don't put an attribute if I don't have a value.
**Aaron Abbott** 19:42 Okay.
Dylan, is that… Does that sound right?
**Madaket Beach (us-cam-5cc)** 19:51 So, I think it sounds like we're just gonna leave it up to the instrumentation to figure out, to decide what to do.
by… Like, it would be good to have, like, a… I guess… Like, in general, Should we put… Like, a default value of zero if we don't have Like, just take any attribute, like, take, like, input tokens.
If, like, input tokens is zero.
Do we add an attribute for it with it set to zero, or do we just leave it off?
**Keith Decker** 20:31 So what I do now for a lot of the… some common app views is, if they say required.
I have them as required on the data class, so that you have to…
**Madaket Beach (us-cam-5cc)** 20:43 required. I didn't realize that.
**Keith Decker** 20:45 Yeah, in Semcov, there's a… it's required If provided.
And then there's a straight-up required. So if it's required, if provided, I definitely… Have to go through and check it, and if it's… None. I don't include the attribute.
But there are a few that, like, model name.
It's absolutely required, so I… I don't let them create the LLM invocation without the model name.
**Aaron Abbott** 21:20 That clarifies things a little bit.
Yes.
Yeah, I think when I talked to Josh… Josh Surrett, I think he… Or, Dylan, when you talked to him, I think you mentioned, like, there's some validation that Weaver, the Weaver tool can do… can do.
based on that, I don't know if it respects the required or not. I don't really love that we have, like, a type system in the YAML for the semantic conventions. I feel like this should be a little bit… Easier to do in a cross-language way, where we don't have to, like, interpret stuff, but, for this topic, I think, yeah, that it makes sense. If it's not required, we can… we can leave it off, like you said, Dylan, and but maybe we could start, like, a thread in Slack, or as Symanteca mentioned issue.
To help understand the interpretation of this, because… Yeah, if there's some validation, we want to make sure we pass it, right?
**Keith Decker** 22:19 Right.
**Marcelo Trylesinski** 22:23 What's wrong with the YAML?
**Aaron Abbott** 22:27 I mean, I don't think it's very… It's very, like, what's the word?
It's not… Yeah, and it's not based on, like, it's kind of just words, you know what I mean? Like… It doesn't seem to have a precise definition of… What not required means, like… Does it mean the type… the key should be there, but the value should be null ? Does it mean the value should be, like in protobuffer, you would have some kind of zero value?
**Marcelo Trylesinski** 22:58 Oh, I see. I see you don't have a schema, you just have a YAML… Okay, got it.
**Aaron Abbott** 23:06 Yep.
So if somebody doesn't mind following up on that, I think that would be good, but it shouldn't block this PR.
**Madaket Beach (us-cam-5cc)** 23:21 So, should it be a bug in the semantic conventions?
repo, or… Does…
**Aaron Abbott** 23:32 Yeah, or maybe we could just start… in the Slack channels, or something like that, but… Yeah, in the semantic conventions repo, I think.
**Madaket Beach (us-cam-5cc)** 23:43 Which Slack channel were you thinking?
**Aaron Abbott** 23:47 There's, like, a Gen AI sem… Sorry, OTEL GenAI Instrumentation, and then there's also a gen… a more general one that's, what is it? OTEL… I wanna say it's otel-Semcom, but I'm not seeing it.
OTEL semantic conventions.
**Madaket Beach (us-cam-5cc)** 24:13 I'll… I'll start a thread in the GenAI one.
**Aaron Abbott** 24:18 Okay. Yeah, that sounds good.
On the other question, though, Keith, I can leave a question… I can leave a comment on the PR, but I feel like if… the most, like, Pythonic way to handle this is… with the, context manager form, so, like.
You don't have to kind of guess if there was an exception, or make some kind of inference based on the parameters that were provided, because it would, you know, explicitly pass the exception that was bubbled through, so… I know we can't do that in some cases, like LaneChain. The instrumentation has to be based on the callbacks, but… I'm assuming you have an exception object that you could pass, which would be more explicit, and it would basically look like the… like the exit.
context manager.
Great.
**Keith Decker** 25:09 Yeah, when we do the context manager style in the telemetry handler.
It does automatically do the fail LLM when when an error has occurred. So, there is an error object that gets passed through, and it will go finish reason of error that way. I think this is more of an issue when Like you mentioned, the langchain one, where… We don't have that information, and they've explicitly called Stop LLM.
Or finish at end, I don't know which one it's called.
But haven't supplied a finished reason.
**Aaron Abbott** 25:47 Yeah, I think my preference would be to make it more explicit and not try to infer it based on the finish reasons also. So either if that's, like, accepting an exception as a parameter similar to the exit, like the double underscore exit that you see for a context manager interface, or… Even if somebody just provides the… Like, an error.
An error type that gets passed in, or something like that, so… I'll take a look, I'll leave a comment right now.
**Keith Decker** 26:14 Okay.
Appreciate it.
So I think that's all I had on that, Pierre. So, appreciate the input.
**Riccardo Magliocchetti** 26:48 Sorry, I have the Zoom web app crashing for the second time.
So, I think we can go on with the next topic.
And… I don't know, file this?
Logger configuration, logger filtering?
Okay.
So I think what? We can skip it for now.
And… Again, from Keef?
**Keith Decker** 27:43 So this one is just a reminder to get some eyes on the adding metrics to the GenAI utils. Mila took a look and mentioned… or noticed that there's a bug in another utility for… generating metric, Oh, what are they? Histograms? Other than that, yeah, just some other eyes on this fruit.
That'd be handy.
**Aaron Abbott** 28:17 Thank you.
**Riccardo Magliocchetti** 28:28 Okay… So, next… Fox seller?
By the freedom.
**Marcelo Trylesinski** 28:38 Yeah, I mean, just… Yeah, just wondering if there are any plans.
**Aaron Abbott** 28:47 Yeah, I think, Alex left.
created an issue for this already, which is great.
I'd just love to comment on there, I think.
I imagine that 314 will be pretty uneventful, but if we test with free threading, I don't know if there's gonna be any issues.
So we should probably… scope in some CI, adding to the CI, the free threading build, and testing everything against that.
**Marcelo Trylesinski** 29:17 Do you do something that, like, can you think of something that would be impacted by this?
**Aaron Abbott** 29:23 I mean, we have a couple places that were clever, so like, you know, relying on Deck, for example.
In a couple ways, but I think most of the things are atomic operations anyway, like.
It should hopefully be okay? I don't know.
It would be good to test it. Is that something you do in Finantic at all, either in Logfire or Vidantec itself?
**Marcelo Trylesinski** 29:47 I mean, Logfire is waiting for this. I don't know, actually, I don't need to ask Alex, If he's asking here, maybe pipeline was failing there with 314?
I mean, because, you don't have the… that requires Python, Python, is that right? So…
**Aaron Abbott** 30:09 Yep.
**Marcelo Trylesinski** 30:11 I don't know.
Oh, Impaidantic, I also don't know. Impidantic is, there is rust stuff, so we need to build the wheels properly, or something.
**Aaron Abbott** 30:21 Yeah, yeah.
Yeah, we don't have any native code, but I think, And if there's missing… we have some things with optional dependencies on wheels.
I think GRPC is… is one of the ones that's usually really annoying, but they probably have 314 wheels out by now, so… Yeah, does anybody wanna… wanna work on this?
**Riccardo Magliocchetti** 30:53 My personal preference will be to defer this to the… after the next release.
Like, or at least, like, don't block the release on this.
But, yeah, like, like, I can take a look at that, but I'm a bit… Overwhelming these days.
Yeah. Like, usually it's not hard, if you're lucky.
It's just a matter of, like, having to rebase or merge must remain on every other PR.
Because of the… the workflow will change, but yeah.
So, yeah, I can take a look at that, but no hurry. Also, like, Marcelo or Alex.
If you want to.
To do that, feel free.
**Marcelo Trylesinski** 31:48 No, I mean, there is no hurry for that. I'm good.
**Riccardo Magliocchetti** 31:51 Okay.
**Marcelo Trylesinski** 31:52 I see what you did there.
**Riccardo Magliocchetti** 31:56 Yeah, no, like, because otherwise, also, like, usually we wait a bit.
**Marcelo Trylesinski** 32:01 Yeah, it's okay.
**Riccardo Magliocchetti** 32:02 because of the… we'll add, like, more minutes to the CI, and so…
**Marcelo Trylesinski** 32:08 Yes, I understand.
**Aaron Abbott** 32:13 Yeah, I was gonna ask you about that, too. Do we usually drop the previous version before we add the next one to keep the window size the same?
**Marcelo Trylesinski** 32:21 I don't really remember. That you… In this project? I don't know.
**Aaron Abbott** 32:26 Yeah, we wrote it down somewhere, I think.
**Riccardo Magliocchetti** 32:29 Yeah, like, usually we… we wait 6 months before dropping, The end of support, release?
So, yeah, it will be, like, next year before we can drop off 3.9.
**Marcelo Trylesinski** 32:47 We should also, I mean, if we do this for Python versions.
Maybe we should also do for packaging supporting versions?
**Aaron Abbott** 33:02 Which, I didn't follow that.
**Marcelo Trylesinski** 33:04 so, like, if a package is more, like, I see, well, at least on some meetings ago, I saw that Starlit had, for example, 0.13 supported, and it's, like, 5 years, 6 years ago or something.
And the code… Changed a lot.
**Aaron Abbott** 33:23 Yeah, I think the problem is it only supports… It doesn't support newer Starlit, so…
**Marcelo Trylesinski** 33:31 What do you mean?
**Aaron Abbott** 33:32 It was…
**Marcelo Trylesinski** 33:32 Oh, oh, oh, I see.
**Aaron Abbott** 33:34 Like, if you drop those two versions, then you would just not support anything.
Which maybe… maybe that's… maybe that's fair, maybe we should, cleanup instrumentations, which are, like, stuck on really old releases. There's probably not a lot of value in them.
**Marcelo Trylesinski** 33:52 I mean, my point was that if we're dropping the Python, then the package would… like, that package for sure doesn't… support, well, I think it doesn't support newer versions.
Of Python.
**Aaron Abbott** 34:08 Yeah, yeah.
**Marcelo Trylesinski** 34:13 Yeah, on my last topic there, this is just… So, completely optional. I don't help much on the repository anyway for a long time. I just don't come here to bother. But, about the… I would like to propose a change of line length.
to… I think this one is set to very short or something, but this repository seems very verbose when I read them.
So, I'm proposing to increase that.
**Aaron Abbott** 34:48 I thought we did increase it.
Maybe it's just the code.
**Marcelo Trylesinski** 34:55 Did you increase it to how much?
What do you mean.
**Aaron Abbott** 34:59 I could have sworn we did this, like, a couple years ago, but I, you know, I'm open to anything, it's just, You know, it'll create a bunch of changes, but… That's okay, I think there's a way to ignore them in the GitHub blame.
**Marcelo Trylesinski** 35:14 Yeah, there is.
I was just bringing up the… what's the feeling?
What's the number?
**Aaron Abbott** 35:22 79, that's short.
**Marcelo Trylesinski** 35:25 Yeah.
That's… yeah. That's, I think, what's the piled ones.
**Aaron Abbott** 35:30 Yep.
**Marcelo Trylesinski** 35:31 Black one's 88, and new stuff, given the typing got a bit too lengthy, are using 120.
Anyway, it was just that.
**Aaron Abbott** 35:50 Yeah, do you mind filing, like, an issue for it, and we can, I don't think it's probably too controversial, but… I mean, the only real downside is it creates… It creates, like.
**Marcelo Trylesinski** 36:02 I mean…
**Aaron Abbott** 36:02 Messy.
**Marcelo Trylesinski** 36:04 Yeah, I mean, I'm gonna invalidate all pull requests, so it's a bit controversial, right? Because everybody's gonna have to rebase.
So, yeah.
I mean, I can even create the pull requests, just, if… if people don't want them… You know, it's just gonna be a waste of time.
But I can create an issue.
**Aaron Abbott** 36:29 Okay, yeah, I mean, anybody who has an opinion on it.
please share right now, please feel free.
Looks like everybody's dropping. I guess that's it.
**Marcelo Trylesinski** 37:22 Okay, see you later.
**Keith Decker** 37:24 Yeah, did Ricardo crash again? Is that what happened?
**Marcelo Trylesinski** 37:27 Have a nice week.
**Aaron Abbott** 37:27 Yeah, maybe it did, maybe we're just stuck here later.
**Keith Decker** 37:30 Alright, so good.
**Marcelo Trylesinski** 37:31 But…
