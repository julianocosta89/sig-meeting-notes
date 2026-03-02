SIG: Python SIG
Date: 2025-07-03
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Ridhima Satam** 01:30 Hi, this is Redhima. Do we have to? So I'm attending this meeting for the 1st time. So just asking, do we have to add our names to the document I see here in the invite, and the topic.
**Riccardo Magliocchetti** 01:44 Yeah, yeah, we're waiting just a few more minutes, and then we start.
So in the meantime, yeah, please add it. Add yourself as attendee to the notes
and welcome, of course.
Okay, I think we can start
so welcome everyone to this week. Python. Sec. Call.
Please add yourself to the signals.
I shared it in the chat. I hope you can see it.
And yeah, if you have any last minute topic, please add went to them notes as well.
Yeah, I think we can start. Can you see my screen.
**Emídio** 06:23 Yes, it can.
**tammy.baylis** 06:23 Yes.
**Riccardo Magliocchetti** 06:24 Okay.
So the 1st one is, we would like to cut release, I guess, next week.
And the blocker right now is missing working semantic convention package.
because the 1.3 5 release of the semantic convention
highlighted some bugs in the in weaver, but is the tools, the tool that is used to build to build the
the semantic conversion.
I've seen that Lyudmila fixed the issue, but we're still missing a release, an updated release from some Comp.
And so we're waiting for that
like we could probably release with the same semantic convention as
as last release. But usually, like we we tend to bump to latest once we release.
And other than that, we have a bunch of Prs
deprecating and renaming stuff around the log for log stabilization.
And yeah, I was looking for having
more opinion from fellow maintainers, but not there.
So yeah, like anyone.
Possibly like the distro people maintaining a distro distros, do you have any opinion on these logs, Renames.
I shared the Erpr.
But it's not the only one. There is another one from the Dylan
but is deprecating the event. Api.
But I think at least, Aaron, be the one to have that right now, like as far as understood.
So yeah.
So if you have time, please take a look at this one.
and yeah, if you like it, approve or don't.
**Pablo Collins** 08:52 Are we taking? Are we taking an intermediate step with this change to deprecate the old names? First.st
**Riccardo Magliocchetti** 09:00 Yeah, this one introduces the new one, but still keeps the old one, but they precade them.
**jeremy** 09:10 Is one just like a pointer to the other. Basically.
**Riccardo Magliocchetti** 09:14 Yes.
**jeremy** 09:15 Okay. Cool.
**Riccardo Magliocchetti** 09:18 So we have the new name, and we have the old name, but you know it's from the
for the correct one, and it's decorated with a deprecated decorative.
and, like the Dylan Pr. Managed to.
Sorry. It's pronounce that the Dylan Pr. But is deprecating the event. Cpi.
Unfortunately, like we don't have the a release already with the
event name attribute for a parameter for log.
and so, but probably could wait at least so at least. But one can update the code
and avoid the duplication. But again.
I don't have a strong opinion about that.
**jeremy** 10:27 I'll definitely be taking a look at this. This is, this is pretty good.
**Riccardo Magliocchetti** 10:31 Thanks.
What kind?
Then? I think we can.
Yeah, we can maybe revise what Emilio added, at least to them
to the topics, because, like last week, I don't ask if anyone would like to share
what we think like we, or a big achievements of the last year, or any plan for us
or anything that it would be nice if the Gc. Or the Tc.
Can take a look at.
So maybe, Emilio, do you want to go through your points.
**Emídio** 11:34 Oh, yeah, very quickly. I think one of the biggest biggest achievements was
like support. The opt-in feature for stable
Http is so much information in like almost our instrumentations, and also supporting Python 3 dot. 13.
And for me at least, I consider, like a big achievement
for my use case the example of this one in core.
I also added the generic stuff, but I'm not sure if how people feel about that.
But I also like something important.
That's everything. I remember that we released in the last year.
**Riccardo Magliocchetti** 12:45 Yeah, thank you for remembering that. Like, I like forgot about the examples. For example.
**Emídio** 13:00 And for next 12 months, I think
this year, in the next one, I think.
we have agreed that it should stabilize logs.
**Riccardo Magliocchetti** 13:19 Yeah, hopefully, we take a lot less than 12 months.
Hopefully.
**Emídio** 13:25 Yeah.
And from the next list I added an issue that is not only related to Sig Python.
but I was. So we can benefit from this one. It was open fornet mutation.
but it's something that we can leverage for sure. Like to do more automations
on our end, like for releases and for request reviews
right now we don't have, like an open telemetry board
with permissions that we can like set labels or things like that.
And most of the
of the things we are doing on the release right now are dependent on adding labels, and would be nice to
so have a proper bot to do that.
To make things more easier.
**Riccardo Magliocchetti** 14:45 Yeah, indeed, it will be great like to
to to skip the clos and reopen Ps. At every release in order to drive and pass.
**Emídio** 14:54 Yes, in the future we can also do things like
contour everything through the comments like setting a slash comment and make something running this guy
like to fix rough or things like that.
**Riccardo Magliocchetti** 15:17 Oh, nice.
Okay, thanks and meet you.
And, by the way, if anyone else has something to add, feel free to add, but
I guess at that I will forward the the answers to the just see.
**jeremy** 15:45 I'm in the process of of updating. But just a small note. My Pr is not finished for this, so I didn't put it on. But I'm almost done with Pr to fix the dependency conflict breaking change that I talked about.
maybe like a month or 2 ago. I just haven't had the the cycles and the the time to work on it until now. Thankfully, it's looking good. It's looking like it can be fixed without regressing on the functionality that
the change intended to add. So because we're about to release, I'll probably I'll probably wait until after the release, since this is a big change, and I want to make sure that all the stakeholders sort of included. That works for everybody.
But yeah, if you're if you're interested in that definitely, check it out and.
**Riccardo Magliocchetti** 16:43 Okay, thank you.
Left me out there like that.
Okay, but we have a Redeemer
on the line. Change language chain. Pr.
**Ridhima Satam** 17:05 Yes, yeah. Hi, so we are trying to introduce. Yeah, this is the Pr, and
we are trying to start supporting the Langchin instrumentation. Gen. AI framework. So this is the 1st pr and we have done some Poc, regarding the complete framework about its features, like, I've mentioned that like the tools and other features or chains. We are trying to create spans, metrics and event logs out of that. And
yeah.
yeah, so this. This basically Pr is just the beginning. It's just few files which are just the project files required. And we took some inspiration from the existing Openai, v. 2. Project like the like, the same Gen. AI framework level.
So just if you go in the file changed file files added, There, it's just the beginning of the project. So nothing, nothing exactly related to Langchain implementation, like instrumentation. But yeah, just general beginning files. Yeah.
**Riccardo Magliocchetti** 18:18 Okay. Thank you.
**Pablo Collins** 18:22 Is this is this? This is this kind of a standard way to introduce a new instrumentation, to create a Pr of just a skeleton
and then add additional Prs later
cause this is, I mean, this approach was when I used to work on the collector, and that was, that was very much the
the the approach, the official approach to creating a new collector component was, you had to have a certain number of Prs.
and, like the 1st Pr. Couldn't contain any actual
logic it just had to contain. Like the skeleton files
I was. I have not gone through the process of creating a new instrument, a a new instrumenter in this repo. So I was wondering how
folks are doing it.
**Riccardo Magliocchetti** 19:13 I don't think we have any official way of introducing instrumentations.
but I guess, like one thing, you may want to create an empty package just for, like maybe reserve, the name.
**Pablo Collins** 19:31 Oh, that's that's that's an interesting point, Ricardo, because the name has already been taken.
**Riccardo Magliocchetti** 19:36 Yeah, yeah, I remember the your.
And so we we like for like for the I think it's for the vertex. AI Aaron, like
talked with the Tracerope people like I am assuming. But let me check
that is open Llmmetry. That is, yeah, but took the name.
And yeah, like for vertex. I think Aaron was able to to admit, like himself, a Maintainer for the packages, so we can release
the vertex AI with the same name.
I don't know if you can have a reach the same agreement with them.
But yeah, otherwise, like, like Openai, you have to change the name shit.
**Pablo Collins** 20:37 Well, if anybody has has any suggestions for how to proceed here like
that that sounds like a good idea, Ricardo, to reach out to the owner of the name that's currently registered.
But if there's any other, you know, suggestions.
**Riccardo Magliocchetti** 20:50 Questions would be to attend the Llm. Weekly call.
where you have the Nirga from open elementary.
so you can get in touch with him.
**Pablo Collins** 21:04 Okay.
**Riccardo Magliocchetti** 21:05 You know.
**Pablo Collins** 21:06 That's that's a good point. Okay.
**Ridhima Satam** 21:10 Otherwise we can just add, like in the end, like v. 2 to it, like open AI, v. 2 has added.
is that a suggestion like, if you will have to come up with a new name.
**Riccardo Magliocchetti** 21:22 Yeah, like, you can follow what Openai did.
And we just wanted to be true. Yeah.
**lechen** 21:32 With reaching out to Gen. AI to use the same name.
So customers won't get confused.
But if we have to, we'll use something else.
**Ridhima Satam** 21:52 So do we have people here who look into projects. So how do we get reviews on this like from this committee right now, who are in the meeting, or do we have to call out anyone? I already see some of the the reviewers have been added, so do I have to just call out there, or How does this go.
**lechen** 22:13 Yeah. Usually you attend the and bring up your Prs directly.
or or reach out to the people directly. It'd be the the ones in the yeah.
**Ridhima Satam** 22:30 I see so so, Pablo, do we know this genetic? Where we where we can find this or.
**Pablo Collins** 22:36 Yeah, yeah, it's on. It's on Tuesdays.
**Ridhima Satam** 22:39 Okay.
**Pablo Collins** 22:40 It's in the calendar.
**Ridhima Satam** 22:41 I see. Thank you.
**Riccardo Magliocchetti** 22:57 Okay.
any other last minute topic we want to discuss.
**lechen** 23:07 Hey? Sorry, Ricardo. I joined late. What was the outcome of the logs? Deprecation.
**Riccardo Magliocchetti** 23:13 Well, I asked, if anyone has an opinion.
and that's it. And I think someone like
said that they carry you with.
But like I think, for for this particular Pr. I think the approach is fine, because when we have the new, the proper code, and the packet one side by side, so it should be easy to.
**lechen** 23:41 Which pr business.
**Riccardo Magliocchetti** 23:43 This is the actual, or it may.
**lechen** 23:47 Okay. Yeah.
Cool. Cool. Sounds good.
**Riccardo Magliocchetti** 23:53 Yeah, but I'm unsure. What's the plan for for the Dylan? One deprecating the events? Api.
because at the moment we we don't have a release with the event name added to the
to the log constructor.
And so it's.
**lechen** 24:20 Yeah, and I think Dylan's not here either.
he's working on it. But the last I spoke to him like he wanted to just get the Api change released.
And then we can start migrating the instrumentations afterwards.
**Riccardo Magliocchetti** 24:43 Okay, makes sense. Yeah.
**lechen** 24:47 And and then we're gonna do the same thing for the deprecation where, like, we just mark old attributes deprecated, and we never break customers. So.
**Riccardo Magliocchetti** 24:59 Yep.
Okay.
Okay.
**lechen** 25:03 Cool.
**Riccardo Magliocchetti** 25:06 Okay. So which were all the topics for today.
Thank you. Everyone.
See you next week.
Thank you. Bye-bye.
**Emídio** 25:20 You, too. Bye-bye.
**Riccardo Magliocchetti** 25:21 Oh, my God!
