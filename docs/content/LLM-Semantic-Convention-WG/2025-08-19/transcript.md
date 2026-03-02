SIG: LLM Semantic Convention WG
Date: 2025-08-19
Duration: 66 minutes
Zoom Recording URL: https://zoom.us/rec/share/E3aTRg5f5ZuT-UPw_6y0yAaDUGM3JsCg7_dOKV29NxKhAmqWVzFswf4jDTdvXHjn.qpwAipocEWjceq3w
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:04:10 Hello, hi folks. I like her too short, Sergey.
anksing 00:04:19 Hello.
Shuwen Pan 00:04:20 Hello.
Liudmila Molkova 00:04:21 Hi, Ankit. Hi, everyone else.
Okay, so let's get started.
I wanted to share my screen…
Please add your name to the agenda, and if you have anything to… please add your name to the agendas, at least. And if you want to discuss something
Please add your… topic to the agenda.
… I…
didn't do this before, but maybe we can try this. There are a lot of people who are joining.
But, you folks don't add any topics, and I'm not sure if you just want to be a fly on the wall and listen in, understand what's going on here, or if you just want to introduce yourself. That would be wonderful.
If not, then it's also fine.
So… Maybe we will add this to the standing topics.
That's just 5 minutes for the optional intro.
on…
Okay, so while we are waiting for people to join, let's take a quick look at the project board. We…
need to do a better job maintaining it. …
So we have a couple of new issues. Let's take a look.
I think this would have been discussed before.
And Ankit, you're actually working on the evaluation results.
In addition to events.
anksing 00:06:26 Yeah.
This is, active work in progress, yeah.
Liudmila Molkova 00:06:30 So, wait….
anksing 00:06:31 Huh.
Oh, this one is an issue that I opened, like, to length. Yeah, I'll be working on this, I want to just, get my ActivePR merged, and then I'll start working on this one.
Liudmila Molkova 00:06:41 So the invalidation results span in addition to the event, or…?
anksing 00:06:46 Yeah, so this was, I think, that came after the discussion that
We can definitely start with, like, events, because that kind of meets most of our needs. And then, optionally, if you want to also have,
It spans for evaluation.
Which could capture how, a score was calculated, and so that needs discussion whether it should be another thing, how do we link it, things like those as well.
Liudmila Molkova 00:07:12 those discounts.
anksing 00:07:13 And I put, like, 3 different major things that came out of the discussion, so….
Liudmila Molkova 00:07:17 Yeah, thanks, I just misread your description, I'm sorry. So, you're mentioning it's work in progress.
anksing 00:07:24 Yes, I'm yet to start work on this after I get my other PR mortgage, yeah.
Liudmila Molkova 00:07:29 Okay, should I assign it to you?
anksing 00:07:32 Sure, yeah, let's do that.
Liudmila Molkova 00:07:34 Wonderful.
And let's see, it's in progress.
Another new issue… yeah, I've all added to the agenda, I'd love to talk more about this.
So…
Cool. So, I see people are here now.
So let's… Move on to the main agenda.
…
Okay, so the first one on Kit 8… oh, sorry, wait. Let's try to practice. Is… is anyone here on the call would like to introduce themselves and talk about why you're here, what you're interested in from genetic observability?
Josh Bonczkowski 00:08:49 I will do that. This is Josh, from New Relic.
So, a couple years ago, New Relic, we started building a AI product around our own agents, not OTEL-based. And then I've been working through the last few months on how to map our interfaces into OTEL.
So we start to expand and kind of support our customers leveraging hotel instrumentation for GenAI within our product space. So that's a lot of what I'm doing here is…
One, listening where… where the GenAI spec is going, so we keep abreast of those changes, as we start to make, update our product to support GenAI.
And maybe at some point we'll have something to contribute back, but mostly I'm here as a fly on the wall, I think, to start with, at least. And we'll see where that goes from there.
Liudmila Molkova 00:09:38 That's wonderful, thank you.
Anyone else wants to introduce themselves?
Shuwen Pan 00:09:47 Yes, this is Shoem from Cisco. I am here to, help out the LLM initiative that Sergey's team is, like, doing.
And, yeah, yeah, that's me.
Liudmila Molkova 00:10:02 Wonderful, thank you. Nice to meet you both.
Craig.
So… I assume that's it.
And let's move on to the main agenda.
Okay, Ankit, do you want to talk about the evaluation results?
anksing 00:10:31 Possibly, yes.
Yeah, so, actually… in the last 6, …
We had an agreement on, like.
emitting evaluation results as events, and then, on the discussion for spans, that's in the other issue, that we just discussed. So, we're going and…
For that, I think the spec looks, almost there in that regard. However, there are some few open comments that I would like to go over and, see if we can get a consensus, and if we can get the PR closed for… from that perspective.
So… And I think there are two, outstanding open comments. One is about…
do we need a metadata field, which is a property bag? And I think there were two reasons why I added this. One was to kind of capture the evaluator ID, which would be
basically capturing the ID of the evaluator, like, whatever produced those scores. And I think in the discussion, I got to know that there is something called
… I forgot the name.
Liudmila Molkova 00:11:45 Instrumentation? That's cool.
anksing 00:11:47 instrumentation scope, yes, yes. So, and I think that can possibly capture that, so if that's the case, then I think I'm good removing that metadata field for now.
Until I have a more concrete example of something which we cannot capture as a, like, a top-level attribute, so… and then, so…
I can do that, like, right after this call, I can update the PR. The other one is about, evaluation… genai.evaluation.label attribute. And… and I think, Limila, you had a suggestion on whether we should name it
Core, genai evaluation.score… dot number, and then score.descriptionRate. So, I think I had some comments about that, where…
I think that gives me a feeling of… the description is basically capturing what this core number is
And when you're defining, like, a…
LLM as a judge matrix, you usually define a, like, a rubric of how LLM should calculate a score.
… So, but however, my intention is not that for that label attribute. My intention is…
The label should be more, like, easy-to-use.
Or easy-to-read value, or a label which customer can just make sense of, even if you are not very well versed with
Like, a data science aspect of it, right?
So that's my intention of that.
Liudmila Molkova 00:13:15 The label, or whatever we will call it, is the interpretation of the score. So the score value can be 42, and the label will give the interpretation of what it means. Is it grounded or not grounded?
anksing 00:13:31 Grounded, exactly, yeah.
Liudmila Molkova 00:13:33 So we actually want both the value And, label.
anksing 00:13:40 Yeah.
Possibly, yes.
Liudmila Molkova 00:13:44 And in this sense, this option would not
work, right? Because you would then need to have a complex attribute.
And I think what I really like about the score, that even without knowing what the evaluator is.
You… you know it's a number.
And you can have some predictability.
So I, I, I think having a complex attribute here Would not be…
Helpful to anybody querying this data.
anksing 00:14:18 Hmm, I see.
Or building metrics, right? So I imagine the most… the most popular use case is building a metric. Metrics, yeah.
Liudmila Molkova 00:14:27 Listen, viewing it as a dashboard, or, like, calculating KB score or something.
And then, having the flat attributes, is very useful.
here.
anksing 00:14:42 I see. Okay.
Liudmila Molkova 00:14:44 But then the label… so my problem with label is that it can mean absolutely anything. So, like, you can imagine, like, a tag on the Azure resource. It can, like, label, tag, it means…
Anything, so can we find some…
name that actually describes, and having it in the score namespace shows that, okay, this is the both properties of score the number, and this
other thing.
I see. Or maybe score label makes it less…
ambiguous, if it's JNA evaluation, score, label, score text, Supporter… I don't know.
Result. Status.
anksing 00:15:37 Hmm.
Liudmila Molkova 00:15:38 Alex, you had some thoughts on this, do you want to chime in?
Sorry for putting you on the spot.
Alex Hall 00:15:45 … Let me also see what I just put in the chat.
Liudmila Molkova 00:15:50 Okay.
Alex Hall 00:15:54 I was also interpreting it as score and label have the same kind of role, it's just that one is for strings and one is for numbers.
The idea of, like, having…
a raw score, an interpretation of a score, and reasoning about the score is weird to me. I don't know how often you get the score being, like, given twice in two different forms.
I don't think that we can restrict score to be between 0 and 1, like, I think that if…
Someone sets up…
their scoring system to be 1 to 5 stars. That should just work, and not have a choir.
Some additional scaling or something?
anksing 00:16:39 Agreed.
I think at this point, like, score is just double, yeah.
Alex Hall 00:16:47 So I'm just, like, where the conversation between you two got to. Is there now a proposal for a way to…
Capture both numeric scores and sort of categorical scores.
anksing 00:17:03 Yes.
Liudmila Molkova 00:17:04 Go ahead.
anksing 00:17:05 Yeah, please go, let me know.
Liudmila Molkova 00:17:08 To my understanding, there are…
evaluations where you would only have a number. There are others where you would only get a…
category, or maybe you can create an artificial number out of the category, but why would you? And there are cases that
Where the… there isn't… a desire.
to…
have a number and interpretation, whether it's a pass or fail. I… I think this is the… the query time concern.
but also… having some… Interpretation be represented on the telemetry?
fits with the category. I feel they are the same.
Alex Hall 00:18:02 But also, I don't like the idea of different attribute names based on the type, if they have roughly the same meaning, but just different types.
Right?
If it was always called score or value.
whether it's a number, or a string, or a boolean.
I prefer that. It doesn't have to be type any, it doesn't have to allow complex attributes, but at least a union of
Common primitives.
Sergey Sergeev 00:18:29 Yeah, on our side, we were thinking about score is magnitude of the signal, so something in the range between 0 and 1.
Basically, which, platform and customers can set their own thresholds to detect, like, to alert on it, and etc. And, additionally, instrumentation side may report,
some Boolean attribute, which should be probably different, have you detected or not, on the instrumentation site, if instrumentation site configured with some threshold.
I think it should be two different, attributes, but…
This is just one way of thinking about it.
Liudmila Molkova 00:19:20 So, if, if the score type…
It's not known ahead of time.
Then, the simple scenario.
Off.
show me… The metric, just the score by… A later name.
Fails terribly.
anksing 00:19:48 Yeah, no, definitely.
Liudmila Molkova 00:19:51 Wait, we….
anksing 00:19:52 Agreed.
Liudmila Molkova 00:19:54 And union type would… would… would be problematic.
Dear.
anksing 00:20:04 Yeah, I think my intention for this was more, like.
Not for matrix calculation, like, the label field, more for, like.
If I want to show this to somebody who is not in the realm of the data science.
Can they just make… Quick sense of it, right?
From that regard.
…
And then, like, as Sergey was mentioning, right, if you have, say, certain thresholds, for example, like, I take this example a lot, where, say, I have a violence evaluator, and then
I have a scale from 1 to 5, and then for me, the threshold is, okay, I'm…
working on some games, so I can have a higher threshold for violence, right? So, I can keep my threshold as 4, and I could still say my score is 4, but my label is passed, because I want that. But for a chatbot, a customer agent.
I would want the threshold to be, like, 1, right, where I don't want anyone thing to come out, right? So, for that.
I could set my threshold, and then I can put the label as, okay.
Non-violent, right, or violent.
So that makes it kind of easy.
For somebody to kind of interpret the results when they're looking at some sort of a… either dashboard or…
Yeah, even… Like, in the tracing view.
Sergey Sergeev 00:21:25 Yeah, and something like, bank AI assistant is quite different from, AI body assistant, they have different thresholds for the same evaluation types.
….
Liudmila Molkova 00:21:41 Is there… is threshold a constant thing? I would imagine this is dynamic. Yeah.
anksing 00:21:48 Yes, and that would be based on, like.
When you did the evaluation, right, kind of.
I would probably, like, value that more if I could just do that during matrix calculation and kind of have these numbers already, and then kind of play around with the threshold, and then set my threshold, right? Those kind of things, not during evaluation time.
That would be my preference, but then I've seen some completion who actually puts you threshold right when you're calculating the score. I've seen those two.
Liudmila Molkova 00:22:21 Is, is there some, …
frameworks that do this, where have you seen it? I'm just curious to know how….
anksing 00:22:31 evolves, like, most of them, they have graders, where when you actually speak a grader, you have to also give a threshold, and they always give you a pass-fail result, like…
Out of it.
So, that's one.
Example.
And, … Yeah, I think… I can look up more, if that helps.
So, I just wanted to, like, check, say, if label field is…
Probably we might need more discussion, looks like. Would it be okay if I…
Just go ahead with the score field for now, and then I can come back to the label field.
Liudmila Molkova 00:23:14 I think we kinda agree that score is not a simple thing.
And… If we just introduce evaluation.score, we will be in the bad position.
So we know there are a lot of things that go into the score, and it can have multiple values, so I wonder if we should proactively
Say it's a number, or a value, or something that would allow us to add more things into the score namespace.
anksing 00:23:49 I see. So far, say, if you have to aggregate this course, right, over time.
Then you have to somehow translate it to some sort of number sign.
Like, even if it's a binarization of yes, pass, fail, you would say either 0 versus 1, right? And then kind of aggregate them.
are… Are there different ways as well?
Liudmila Molkova 00:24:11 I would imagine that if you want to build a dashboard that shows numbers, you would look for all the events that have the score number set and build
The visualization based on this.
And, I think it's a good question whether we will force instrumentations to report a number, even if it doesn't make sense. I don't…
I like this idea. So maybe we would have score.category.
And then, if you would like to build a… I don't know, the…
treat each category as 1, value 1, and then build, like, the number of times you've got this category. That would be a different…
Query you write for those.
And different visualization you provide. But then you, you, you know what…
you have something definitive. You know that you're either dealing with numbers or with categories.
anksing 00:25:15 So, categories is the classification case, right? Kind of, if you have multiple buckets.
Liudmila Molkova 00:25:20 Yeah.
anksing 00:25:35 But then, you would also need information about what different buckets are, right? And what….
Liudmila Molkova 00:25:43 You just column the number of them?
Whatever they are. You don't need to know ahead of time what they are.
To write a query.
Like, you don't need to know a door, oral devilation.
the later names. You just show the number, based on… But by the later name.
anksing 00:26:12 I see.
Yeah, which is the, … Oh, by evaluating Trick's name, I see.
Okay.
I mean, that should work. So… so score.number, I think that seems like something which we can…
that won't… like, we can still extend that if needed, right? Adding more…
score.category or things like those, right? Yeah, I think that sounds like a good idea. Yeah. In future, if you want to expand that, yeah, that's possible.
Liudmila Molkova 00:26:50 Okay.
anksing 00:26:52 So, what… score.number, score.label would sound… would that sound reasonable?
Or… Label is not that sticky, but yeah.
Liudmila Molkova 00:27:08 square.label sounds fine to me, already. I wanna see in, in, in this, community, if we kinda…
see the intent behind it, common.
That we would classify the… score.
anksing 00:27:29 And provide the….
Liudmila Molkova 00:27:32 human-readable interpretation of the score? Is it a common scenario?
anksing 00:27:40 I see.
Okay. Yeah, definitely, I think I can, …
I've gone through some of the compilation which does it, and it's very helpful.
I've gone through Arise, MLflow, Galileo, All of them have this.
All three of them, for sure, and I can, like, look up more if that helps.
Liudmila Molkova 00:27:59 Oh, nice. Would you mind, like, adding, just a few links here?
anksing 00:28:03 Oh yeah, definitely.
Yes.
Liudmila Molkova 00:28:05 Thanks a lot.
Okay, so let me… Right, some notes here…
Actually, I had some thought that maybe you score that value?
Well, yeah.
anksing 00:28:40 Yeah, I think it's go to 12, sounds good to me, yeah.
Liudmila Molkova 00:28:43 And we can, in theory, if we ever find a way to normalize them, we could have scored that normalized value.
From 0 to 1, or whatever.
Got it, yeah.
I don't remember which one of them, but he'll add links,
anksing 00:29:29 Yeah, I can, I can share that. I think, I can put that in a Google Doc and share it here.
Liudmila Molkova 00:29:39 And if you just leave a few comments on the PR, it would be easier to discover, or if you want to share Google Doc, that's also great.
anksing 00:29:48 I see, okay. Yeah, I can find that, yeah. I'll put that together, like, there'll be, like, at least I can put, like, 3 of the competition which does something similar, so…
Hello.
Okay. So, score.number or score.value, I think score.value sounds… Pretty good to me.
And score.label, would that be okay to go forward in this PR?
Liudmila Molkova 00:30:19 It sounds good to me if it's a common scenario, and it sounds like it is. I'm curious if people have opinions here.
Josh Bonczkowski 00:30:33 I do think we need… we will need a text field, whether it's a human-readable label, like, earlier there was a discussion about being able to put in a longer phrase in there.
In other cases, like content, safety or content management, where you end up with a categorization of, you know, is this…
What type of, …
validation did they do, and what is the score of that, right? If that can go on the label as a text, and then the numerical value as the value, like, that works.
For at least the use cases that we've been planning on.
anksing 00:31:12 Okay.
So then, sounds like score.value or score.label would kind of work for that, right?
Do they understand the right choice?
Josh Bonczkowski 00:31:20 Yeah, I think just having a label, having a text field, the label will be fine for that case. Like, these are… the label would be the output from, like, in this case, an LLM coming from somebody else, telling us, kind of what their label and scores are anyways. So, yeah, that works.
anksing 00:31:37 Oh, I see. Is this a human feedback?
Example that you refer to, Josh?
Josh Bonczkowski 00:31:43 So we've been looking… no, not necessarily human feedback, so that's a separate use case, separate scenario, I think, than this one. We do have that as a thing for our customers, but we also have the ability to take all the messages and feed them through another LLM, basically, to determine whether.
anksing 00:32:02 I see.
Josh Bonczkowski 00:32:03 Did you or bias, those kinds of categorizations.
anksing 00:32:05 It is.
Josh Bonczkowski 00:32:06 And getting back a feedback from that particular model.
anksing 00:32:10 eyes.
Josh Bonczkowski 00:32:10 So, that fits in well with here, with having a label and a value.
anksing 00:32:15 God. Okay, yeah, I think that sounds good, yeah.
Liudmila Molkova 00:32:26 Okay.
Do, like, last question on this. Do we…
Have any thoughts on whether the…
Category and label are the same thing.
Would we… assuming we have a category, like.
And there are different grades of, content being unsafe, right?
… Would we envision that If I report a category, It will be… In addition to a label.
anksing 00:33:07 It's possible.
And I think, at least at Microsoft, we have seen that scenario where we try to kind of have bucketized things for customers, like content safety versus AI quality, right?
That can kind of give them an idea, okay?
all the content safety related things go in here, right? And then you can have a category around that, and say violence, sexual, and many more, right? Or toxicity, things like those.
And then for AI quality, like, oh, is your relevance grounded? Things like those, which kind of make your…
So, I don't know. In a way, it kind of fits there where I could say, hey, this category is, content safety, and I could filter things out by that.
Or it's related to AI quality, right?
And then something could be around cost as well, which could be… Something.
But yeah.
Liudmila Molkova 00:34:01 Okay, and the… okay, one more question. Do you envision it… it… it to be…
a string or an array, because….
anksing 00:34:12 Like, there could be multiple….
Liudmila Molkova 00:34:15 categories. The content is toxic and is violent.
And something else. Yeah.
anksing 00:34:22 Yeah, so there, I think I would, like, I was envisioning more, like, categories content safety, and then you have different, evaluation scores, one for toxicity, one for violent, and then your label would be violent, non-violent, toxic, non-toxic, right? And then category would still be content safety, that's what I was thinking about.
Liudmila Molkova 00:34:40 And would we report evaluation result per this thing, or would we have multiple labels on the same evaluation result?
anksing 00:34:51 So, different scores for different… I'm not.
Okay.
Liudmila Molkova 00:34:56 There will be a score per… okay.
anksing 00:35:00 Yeah.
Liudmila Molkova 00:35:08 Okay.
So, thanks a lot for the discussion.
Let's continue on the PR.
And let's move on to the next topic, which is….
anksing 00:35:22 Thank you.
Liudmila Molkova 00:35:24 We are ready to merge the monster.
The refactoring on the chat history. So we have all the approvals, we have all the comments resolved.
And then it can actually merge it.
We've presented it yesterday on the semantic conventions call.
The tooling and the way we define types.
Might go through some changes in the future, but it should not affect anything that instrumentations
produce, it's just the way how we're recording currently in the JSON schema. Ideally, we should have some…
Semantic Conventions tooling to describe attribute types.
Was this… I'm going to merge it, actually.
And I… Was thinking, … But what should come next? There are a bunch of follow-ups we've got.
And I wanted to get your folks' opinion on what should we do. So the first action item for me would be to go ahead and implement this in OpenAI instrumentation, unless somebody else wants to.
But that's the easy part.
the spec part… is more interesting.
So the follow-ups we had is… First, we removed their references.
Definition of references from the pull request.
And now the upload process is completely custom. If you want to upload the stuff somewhere else, you figure out how to record the reference to it.
We can work on this. The other thing… We've postponed is…
adjunct chat history, and I think there were pull requests on this, a lot of discussions.
We should figure it out, and I added…
Related issue to the agenda.
The built-in tools, we didn't figure it out. And finally, the pure extensions, like multimodal content and stuff like this.
… So… I… I'm kind of curious what people here think we should tackle next.
Out of these follow-ups.
Aaron Abbott 00:38:03 Yeah, ….
shiprajain 00:38:04 Isn't it?
Gregory.
Aaron Abbott 00:38:08 Yeah, just real quick, I was gonna say that, my coworker Dylan.
He's working on the instrumentation for the Vertex AI.
…
SDK instrumentation, not the Google Gen AI one, but we can definitely follow up with that one, so we should have,
So, at least an implementation there.
And, …
Yeah, I'll just say I'm interested in definitely the refs and upload, and also the multimodal. I feel like
…
the multimodal should be a fast follow from, like, the refs and upload, maybe. Or we could do it in the other order, I don't know.
They seem kind of tied together, but yeah.
Liudmila Molkova 00:38:50 Nice.
She pretty much say something?
shiprajain 00:38:54 Yes. So, Lydna, I am continuing on my PR, which was for agents' input and output. I have, fixed the comments that I've received thus far in my local. I'm just checking a few more things. So, agent input and output is one thing that I would…
I want to continue with the help of my PR, and now that your PR is also merged, I'm going to take reference of some of the attributes from there.
For built-in tools, I wanted to understand how that is different from, say, the execute tool, span.
….
Liudmila Molkova 00:39:27 And the input and output.
shiprajain 00:39:29 For that, because in my PR, I'm covering both agent, invoke agent span, input-output, as well as built-in tool.
Oh, sorry, tool… execute tool. So, so yeah. How is built-in tools…
A different tool, execute tool span.
Liudmila Molkova 00:39:46 Yeah, that's… that's a great question. So, …
The built-in tool, when you get the output back.
You get all the information about the output tool call, and it's kind of merged together, the request to call the tool, and there is, like, the tool outcome.
And we tried doing the exercise, there is a long discussion somewhere on this PR, …
Yeah, it's merged. There is a long discussion somewhere on this PR,
with a lot of details, I can try to find it. …
I think maybe I'll, like, started it.
Or maybe Sam started it.
Been a very long discussion.
Okay, I'll try to find it and share it with you, but essentially.
shiprajain 00:40:57 Excuse me.
Liudmila Molkova 00:40:59 Non-trivial.
on how to… represent the built-in tool in the current structure.
And there are multiple ways, so we'll need to figure it out.
shiprajain 00:41:19 Okay.
Liudmila Molkova 00:41:19 Oh, Alex had the… All right, it's wonderful, Alex has captured the discussion. Thanks a lot.
shiprajain 00:41:32 Okay, so, the reason why I'm asking this is because in my PR, I'm suggesting the input and output for both executeToolSpan and, agent input output. So, would you suggest to also, cover built-in tool within that, or shall we just keep the scope small?
to begin with, and… and try to conclude on that, we are separately, because built-in tool could… could require more discussion.
Liudmila Molkova 00:41:57 Since we are, …
I think this is orthogonal, right? So, if we find a way to capture built-in tools, it would apply, I hope, consistently to agentic chat history and LLM chat history.
But I think we should discuss this first, like, how much in common do we see between these two, and there seems there is some ground for discussion.
shiprajain 00:42:28 Got it.
And, okay, so then I'll continue the current scope of my PR, without digressing, and, while I present next, in the next call, maybe, if anything additional with respect to building tools should be taken care of, then we can discuss that.
Liudmila Molkova 00:42:50 ….
shiprajain 00:42:51 For multi-model content, also, with respect to agents, I was taking a look. I wanted to keep the PR separate for that, but from my side, that is going to also fast follow a proposal on how to capture multimodal content in agents.
Liudmila Molkova 00:43:07 Yeah, I would love us to start with the LLMs, and unless we, by that time, we merge LLM and engine chat history into one story.
Huh.
There was some comment. Nice, Alex.
Okay, so, ….
Alex Hall 00:43:34 As an example of what it could look like in that issue.
Just something… Yeah, the multimodal.
At the very end. Those are examples of, like, the raw data, I meant.
The last comment in the issue.
Like, this is what a part could potentially look like.
Liudmila Molkova 00:44:01 Nice.
Cool, so I just wanted to start thinking what's coming next. We already have a lot of things in progress, and let's…
we spent some time at the end of the call to discuss the adjunct, history differences. So let's move on…
To the next topic, Tarant, I think you already know what you're looking for. Do you want to present, or do you want to talk about it?
Trent Mick 00:44:34 Yeah, I'll just talk a little bit. This is sufficient here, so… Elastic had…
where I work had an instrumentation for OpenAI for JavaScript.
And we're upstreaming that, or hoping to do so to the OpenTelemetry.js contribib rep repo.
The preference for…
OpenTelemetry.js Contrib is that there are code owners for each of the instrumentations that are there that can be the, kind of, the first line for…
Doing maintenance on things that are
like, specifically about that instrumentation, as opposed to, like, the generic stuff, like keeping linting and whatever, you know, hotel side changes alive. So, I'm asking here if there's anyone that would be interested in being a code owner of this JavaScript, instrumentation. As it stands, it'd be me, and I have some
background on the GenAI side, though I don't have as much bandwidth to follow the GenAI semantic conventions changes. I'm a no-tel.js maintainer, so on, like, handling the JS side issues, no problems at all there.
It would be great if there was someone else who's more involved in the GenAI SIG, or on day-to-day GenAI connections. I wanted to help out there, so…
Let me know, we're happy to answer questions if people have.
This would be the first GenAI-related instrumentation that gets into a hotel.js can drop, so it'd be kind of a nice start.
Sergey Sergeev 00:45:59 Yeah, I hope you got… I didn't take it, I hope you got a review from the Splunk, …
JavaScript instrumentation, …
folks, at least as they tried to review it, but, on Spoenk's side, we have an interest, in helping with those efforts.
Liudmila Molkova 00:46:20 Would you be willing to, share the maintenance burden? Be the component owner?
Sergey Sergeev 00:46:27 Yeah, we do. Again, it… I think it will be happening
As part of this group, we have some anti-convention changes, and etc.
I guess we will have to talk about how we implement changes.
in JavaScript convention, because, … In Python, we at least have an idea of that shared GenAIOT use.
Where we can… I saw it, those changes to telemetry.
probably we need something similar for JavaScript, or since it's the only instrumentation library, maybe we can just keep it in it, but yeah, we… I'll double-check with the folks and try to bring them here to commit.
Do the swipe.
Liudmila Molkova 00:47:23 Yeah, wonderful, and I think, Trent, correct me if I'm wrong, but what you're, looking for is somebody who can be a component owner.
Like, who can review requests? Like, there is a… it's not that you need to commit to doing a lot of Gen AI work, but more, like.
…
your name would be under the OpenAI instrumentation here, and if there is a pull request or the issue created against it, you would be on point for… to review or fix some critical issues. Is this right, Trent?
Trent Mick 00:47:58 That's right. Yeah, it's usually not critical issues, it's usually, like, someone makes a suggestion for, here, I want to add this feature, or change the telemetry that's coming out of this instrumentation, and usually
the component owners here are meant to be the subject matter experts on that, and so they're kind of first point for asking questions. And if it's just generic instrumentation stuff, then that's something that the hotel.js maintainers would handle, so…
Hopefully the burden's light, but basically looking for having experts in the In the individual package here.
Liudmila Molkova 00:48:32 And it seems this Splunk person who reviewed the request is the component owner on some other things, so they know what it takes.
Trent Mick 00:48:42 Always, … Sarah, what was his handle again?
Liudmila Molkova 00:48:46 Seem… okay?
Trent Mick 00:48:48 Does… does he work at Splunk?
Liudmila Molkova 00:48:51 Supply at least his profile says so.
Trent Mick 00:48:57 Okay, great, yeah, …
I just know them from other interactions on HotelJS, I didn't make the connection that they were.
Okay, okay. Do you… do you work with them, Sergey?
Sergey Sergeev 00:49:10 Barely.
Trent Mick 00:49:11 Yeah, okay.
Sergey Sergeev 00:49:12 I relate the request, review the pull request, and got commitment that the team can dedicate some time for GenAI efforts and instrumentations.
Trent Mick 00:49:27 Okay, okay, cool. So maybe I'll tag you or, CMK on that… on that bill request, so you guys are even there for the discussions, whether or not you're able to commit.
I know we can discuss that.
Sergey Sergeev 00:49:40 traded.
Trent Mick 00:49:42 Okay, great, thank you.
Aaron, did you have something on this, or…?
Aaron Abbott 00:49:46 Oh, why don't you go ahead, Lamela? It was a slightly different topic.
Liudmila Molkova 00:49:50 Yeah, I just wanted to quickly check if you tagged Paul, Paul Shelley from Microsoft?
I know Microsoft had some thoughts on maybe we should participate in this. I don't know where it landed. Are you folks in the discussion? Should we ask?
Ankita Shipra, too.
Pink hole and check with him.
anksing 00:50:14 -Oh.
Yeah, yeah, definitely I can check, with them. So, this is for the JavaScript rest together, right?
Trent Mick 00:50:20 That's right.
anksing 00:50:23 Yeah, I can check with all.
Liudmila Molkova 00:50:25 Thanks a lot.
Trent Mick 00:50:29 Thank you.
Aaron Abbott 00:50:30 Yeah, Trent, if I could just ask you a quick question, too, like, being a code owner on this, does it require being part of, like, the JSContrib approvers? I'm wondering from, like, a maintenance perspective, because…
Just the process we have is maybe not as sophisticated in Python.
Trent Mick 00:50:48 I think we changed that recently because…
Something about permissions made it easier to be part of a certain group, but you don't…
My understanding, you don't have to, like…
prove yourself to go up through the levels to… to triage or approver. I think anyone who's signed up to be
the code owner of one of these instrumentations, yeah, you'll get added to…
one of the lower-level groups, just because that helps with the GitHub assignment and machinations a little bit. Does that answer your question?
Aaron Abbott 00:51:21 Yeah, a little bit. Maybe I'll just reach out to you on Slack, and we can chat.
Trent Mick 00:51:25 Sure. Yeah, sounds good. Thank you.
Aaron Abbott 00:51:28 Cool, thanks.
Liudmila Molkova 00:51:30 Yeah, thanks a lot for bringing it up and, doing all the work to upstream this.
Trent Mick 00:51:35 And it looks like the previous agenda item means that this thing will be instantly out of data in semantic conventions, so I'll have to…
Enough, dude.
Liudmila Molkova 00:51:44 That's the constant pain, you know.
Trent Mick 00:51:46 step.
Liudmila Molkova 00:51:50 Okay, so moving on to the link chain instrumentation, Sergey, do you want to talk about this?
Sergey Sergeev 00:51:58 Yes, I can quickly chat about it, so it's, …
something created by one of my team members. Dimash could not join the call today, so she asked.
Me to represent, this pull request.
And, specifically, this is the semantic convention, which will be coming out.
And it's still using, … I believe, … the previous…
No, never mind. I think it should be up to date with the current spec in the semantic convention.
And this adds, just overwhelming vacation.
… instrumentation.
Yeah, I change an AI system.
Liudmila Molkova 00:52:52 Sometimes it's mixed, but yeah.
Sergey Sergeev 00:52:57 ….
Liudmila Molkova 00:52:58 So this is the layer in length chain that instruments, like, the low-level call to the model, and it's kind of synonym to the enabling OpenAI instrumentation. So you would enable one or the other, but maybe not both. That's a fair assessment.
Sergey Sergeev 00:53:19 Sorry, say it again?
Liudmila Molkova 00:53:21 this, this is… actually mirrors the, let's say, uses langchain with OpenAI.
You would enable either the GenAI… sorry, langchain instrumentation or the OpenAI instrumentation, but probably you don't want both, because they are kind of duplicative.
There's this layer, right? Not the logical framework layer.
Sergey Sergeev 00:53:49 Yeah, again, in, in general, the thinking is that,
Right now, I was thinking that we will duplicate both, why you may want to have both plans, or just not use, for example, OpenAI instrumentation. You can use the same location with one chain with different providers.
And, in some cases, OpenAI will provide more
Details, like server others where you make a call, it may be not available in Wangchin.
Callback, … … Yeah, it…
maybe, of course, as Aaron specifically mentioned, that token usage may be double-counted if you count at the trace level.
Then you may get, …
This is double-counted, and it's a question, do you want to deduplicate,
On the backend, on the platform side, or do you want to… … To implement, something…
In instrumentations that they play while together, and what will it be.
Basically, … on the instrumentation side, what will be the mechanism, to…
disable some of the spans if you know that there is more concrete instrumentation. I think it will be something we will need to solve
Maybe later?
for now, I would go with duplicate… not duplicate, but, …
spans from both Lankchain side and child spans from OpenAI side.
Liudmila Molkova 00:55:55 Yeah, I mean, my question is more like, let's imagine that there are… the two tools are configured.
So the span you're capturing is actually the span that represents this call, and if the two calls are happening, they… they will be….
Sergey Sergeev 00:56:10 part of….
Liudmila Molkova 00:56:11 That's fun.
Or is this instrumentation applies to internal operations between Langchain and OpenAI is the key? So, which layer does it capture?
You know.
Sergey Sergeev 00:56:26 Yeah, it should capture just LM on vacation, and two will be added with the next pull request. Again, we're trying to break down, … Yeah, yeah, I'm just asking what is the layer, not what are the features, but would the span….
Liudmila Molkova 00:56:42 capture the duration of the first LLM call, total on vacation, the next LLM call.
Or the spend being added now captures the… each individual OLM call.
Sergey Sergeev 00:56:56 No, I think it should capture just individual OM calls.
Liudmila Molkova 00:57:02 I see. So this is not the same as this call.
Sergey Sergeev 00:57:08 I will need to double-check, I got the idea, I…
I think I need to deep dive into it. I will take a note.
Aaron Abbott 00:57:21 I think, … The tool calls wouldn't happen with that lane chain thing, like…
My brief experience with Langchain and LaneGraph is you have to use, like, the create graph agent if you wanted to do the automatic tool calls.
So I think that one would just call an all-m, but if you did that, …
What would be the case, Sergey, if you use this with LaneGraph with the React agent?
Sergey Sergeev 00:57:43 Yeah, for the agent, we will need to emit, span with, each operation.
So, for example, if you…
Invoka 2, you need to emit, a span for 2 invocation, and so on. And I believe,
What people do is they flatten those pants in the same level, so they don't make two on vacation call a child of the original LM on vacation.
I think this is how it works, but in one chain, it will be another
different construct. For agent invocation, I think you can make all of them
A child span of the agent and vacation, but not… … like, LM orchestrator call.
If it makes sense. But, we will work on it in more details, once we get to…
agent invocation span, and 2 invocation span. So this is just for LM invocation span.
Liudmila Molkova 00:58:57 Okay, cool. Thanks for the clarification, I'll take a look, and probably will play with it.
We are short on time.
I kinda wanted to start this discussion, … As soon as possible.
So, the discussion we had in the past, that we are… we just introduced Gen AI, let's say input messages and output messages.
And ideally, we should have the same attributes capturing the history for …
LLM calls, and for agent calls.
Because the line is blurry, and because it's nice to be consistent. But it seems like there is a…
It's, it's, it's controversial.
… Erin, I think you raised in the past that you think they are semantically different.
And I wonder, why do you think this? What is different?
Aaron Abbott 01:00:05 Yeah, I mean, I… I… I think….
Liudmila Molkova 01:00:11 Like, from the….
Aaron Abbott 01:00:12 developer's perspective, they probably think of, you know, the thing that's actually doing the inference, taking time, running on the GPU.
You know, versus, like.
an agent which maybe delegates that to something else. It feels kind of like if you call an API that uses a database.
is the API the database itself, right?
So, I don't know, like, …
maybe it's not a super big deal. I also saw Shipra, you had your hand raised on this.
shiprajain 01:00:44 Yeah, I think I'll have to… I raised my hand slightly, sooner. I'll take a look at this, issue. However, I was exactly thinking the same thing as Lyudmila mentioned, to, use input, GenAI input messages and output messages as part of,
Invoke agent span to begin with, because the format of the input and output, how we want to accept for an agent, seems similar.
… So… That was one quick point I wanted to mention.
Alex Hall 01:01:17 I mean, Shapraj, as far as I remember, when you're working on the agent stuff.
For you, the inputs mean the things that are given to the agent in the first place, and the outputs are the final result, but the intermediate chat messages don't go in either.
shiprajain 01:01:31 Yes, because we didn't want to duplicate that.
We understand that those intermediate messages are anyways covered as part of the chat history as the LLM response. So, taking that, also pushing it as an output to the invoke agent span would be duplicate.
That's why we consciously decided not to add.
Chat history as part of… yeah.
Alex Hall 01:01:57 I thought it was also about, sort of, like, a semantic…
Differences. Viewing the agent sort of like a black box function.
shiprajain 01:02:04 That's right.
Liudmila Molkova 01:02:12 And Shapra, remind me, which frameworks are we based on? The semantic kernel?
What else have we validated for that approach?
shiprajain 01:02:24 So we have tried it for somatic hurdle, and we are trying for, …
Langraph, I have to check back on Langraph, though. So yeah, semantic kernel was the main one where we proved this.
Liudmila Molkova 01:02:38 Okay, and then, …
Aaron, do you think, like, what are… like, the difference between API, it's effective with the difference in the framework API, or it's an LLM API?
Would you have some candidates that we need to check?
4. Accept multi-cardinal and Langraph.
Aaron Abbott 01:03:05 I mean, I'd like to take a look at A to A, right? Like, I think there's some extra parts of that protocol.
Kind of like, you know, like, capturing state, stuff like that.
Liudmila Molkova 01:03:15 Binge.
Aaron Abbott 01:03:16 There's also…
I'm honestly not too familiar with it, but it seems a little different than the input and output that goes to inference, and maybe we would capture that stuff in different attributes?
I think, just to be clear, though, my, like.
My comment wasn't so much that
I have an issue with the input and output being on the agent. It's more just, like, if we extend, you know, GenAI inference client.
it's kind of like, you know, agent is an inference, which I don't think is necessarily true. I don't have an issue with the actual keys being similar or the same.
Liudmila Molkova 01:03:49 Okay, cool, I understand your concern. Now, I actually am super curious about how it would play out with A2A, and I actually want to learn it, so I would like to take connection item on.
Aaron Abbott 01:04:14 And actually, I also updated the issue description to link to the comment thread from the original PR. I think it was something Alex raised, like, I thought we decided to postpone this, but there was, like, a conversation on it, so I don't know if you saw that, but I did update the issue.
Liudmila Molkova 01:04:31 Okay, wonderful. Thanks a lot, they'll take a look.
Okay, we are, out of time. Again, thank you all for the great discussion and the progress.
Let's see what we can do going forward.
See ya.
shiprajain 01:04:49 Bye-bye.
Liudmila Molkova 01:04:50 Thanks, bye.
anksing 01:04:52 Beautiful. Bye.
