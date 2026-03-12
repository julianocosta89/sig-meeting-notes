SIG: End-User SIG
Date: 2025-10-23
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/-GWKCIXYrAgSsqIbEPd6FrKdVkRVFMJWq-ZAwzlKP_FYUCoy3NumIl-v_T_M-_Fc.ijOo7Rjlka-M_uqc
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 01:28 Hello, hello?
**Ernest Owojori** 01:47 I done… I under…
**Andrej Kiripolsky** 01:49 Hey, I'm doing. Al?
Can you hear me?
Yes, no? Yes, wonderful, wonderful.
**Dan Gomez Blanco** 01:57 We can hear you, okay.
**Andrej Kiripolsky** 01:59 My microphone?
Never happened to me before, but my Mac… started, like… there is, like, a feature in… on Mac when, like, when you close it.
Like, physically blocks microphone, so you cannot, like…
**Dan Gomez Blanco** 02:16 Hmm, I see.
**Andrej Kiripolsky** 02:17 Yep.
And, somehow it started… like, it just didn't stop blocking. So I have to wear the headsets, and I always have to do the audio, setups. It's very annoying.
Yeah.
Dan, how are you? You've been out for a while, right?
**Dan Gomez Blanco** 02:37 Good, yeah, I was on holiday for… 3 weeks?
Two and a half weeks. Nice. But yeah, two and a half weeks, but I missed three of these, I think.
Or 3 weeks in… of meetings, and then, yeah, and then I went… to… I was at InfoQ Dev Summit.
In Munich.
Last week.
**Andrej Kiripolsky** 02:59 Okay.
**Dan Gomez Blanco** 03:01 and then KCD, UK.
**Andrej Kiripolsky** 03:06 Yeah, I just returned from Munich, like, just really, like, 2 hours ago. I was at PromCon.
So, yeah.
**Dan Gomez Blanco** 03:14 Cuckoo. Nice.
Very good. Yeah, so basically I just came back from, from… Holidays straight into.
into conference season, which I'm not sure.
Good idea or not, but, like, you know.
Yeah, as I said, like, you know, why don't I take 3 weeks bef- you know, 3 weeks off?
Literally with no internet in the mountains, and then go into conference season. I'm not sure that was a good idea, but…
**Andrej Kiripolsky** 03:41 This must have been a big, like a… Shock. Yeah.
**Dan Gomez Blanco** 03:46 No, but it's all working out quite well, so…
**Andrej Kiripolsky** 03:48 There you go.
**Dan Gomez Blanco** 03:49 good.
Hey guys!
**Andrej Kiripolsky** 03:55 Hi, Adriana.
**Adriana Villela** 03:56 How's it going?
**Dan Gomez Blanco** 03:58 Dude.
**Adriana Villela** 03:59 Dan, you're alive!
**Dan Gomez Blanco** 04:01 I'm alive.
What did you take? Like, you know, I went through, like, a lot of hiking, I was like, you know, just been through the mountains and blah blah blah, and I just get back, and, like, I'm just sleeping in a, you know, different bed.
I woke up today with some really, really bad neck pain. I was like.
**Adriana Villela** 04:18 Oh, no!
**Dan Gomez Blanco** 04:19 This is what you're supposed to get when you're hiking, not when you're, like, you know, sleeping in a slightly different bed.
**Adriana Villela** 04:24 That is so funny.
**Dan Gomez Blanco** 04:25 We're not getting… we're not getting any younger.
**Adriana Villela** 04:28 I know, I know, I know. Yeah. After I hit 40, I was like, my body just hates me, and there's nothing I can do to make it love me anymore.
**Dan Gomez Blanco** 04:38 Oh, yeah, I was like, sleeping, you know, or like, you know, it used to be, like, you can sleep on the floor, everything's fine, and now it's like, oh, this is a slightly different pillow, and then your body will be like…
**Adriana Villela** 04:48 Yeah, the body rage. I mean, yeah, I can't even sit for more than an hour without my butt screaming at me, so…
**Dan Gomez Blanco** 04:57 Guys.
Alright, now, we've got quite a lot of topics on the agenda. Yes.
**Adriana Villela** 05:04 Sorry, I added a whole bunch last night. Nice.
**Dan Gomez Blanco** 05:07 I have one as well.
**Adriana Villela** 05:09 Sweet!
**Dan Gomez Blanco** 05:10 I need to ask.
**Reese Lee** 05:16 Hi, everyone!
**Dan Gomez Blanco** 05:17 Hello, hello?
**Adriana Villela** 05:18 Hey!
**Andrej Kiripolsky** 05:19 Hello.
**Reese Lee** 05:21 Oh, weird.
My camera is still not working.
**Dan Gomez Blanco** 05:35 Right, so I'm happy to lead, and I'll think… Go for it. But I think, Ernie, I can share my screen if you want, one second… Righty.
Yeah, Ernest. Do you want to start with, first topic?
**Ernest Owojori** 06:03 Hi, everyone. I was not prepared to start.
Well, let me just… let me just go on. So, we wanted to… what I'm gonna say, I wanted to present… the current progress with, the OTE collector follow-up survey.
and communicate what the next step is. I will just… I guess I should just go ahead and share my screen.
**Dan Gomez Blanco** 06:28 Yeah, go for it. Let me just stop sharing.
**Ernest Owojori** 06:31 Okay.
Please, can you confirm me if you can see my screen?
**Andrej Kiripolsky** 06:47 Yep.
**Ernest Owojori** 06:48 Yeah, so before I go to the main analysis, I wanted to communicate just a bit of the process we are designing into the analysis plan.
The plan is that most of the analysis should be concluded in a document that records the analysis plan, right from the point of creating the survey, but because, This was not in place as at the time the collector's survey was being designed.
So we just keep the question part, and just go out to the analysis plan. I wouldn't necessarily go into details for this, but I will just show these sections. This is just to communicate what the general idea should look like, and data cleaning will also be communicated, but my own process with data cleaning, especially with Google Sheets.
It's for me to be done.
with basic EDA, and I communicate how I'm cleaning, because I believe EDA will show me places that I need to clean, then I communicate that later.
So I've not populated this part, so that's why it's TMT. But that, you know, will be the first section. Then afterwards, we communicate what the general idea looks like, the kind of graph we should be presenting for each type of questions that are in the survey, and you know.
if this goes into plan during the planning phase, people can agree and disagree on whether this will work or not. Just ignore this part, I was trying to make a draft with this. Then afterwards, we want to see the kind of cross-stablishments that are possible depending on the sessions that are in the survey. So, for this particular survey, we have the adoption part, then we try to ask some questions, then we have the other questions that follows under adoption.
Then, afterwards, we have the deployment practices, you know, just ask questions like, does team type really, really affect the kind of deployment environment that people do based on the survey responses? Then, let's say components did as well. For example, we have those organizational sites really of maturity affects the use of processors, connectors, and stations for this case.
And so on and so forth.
So let me just go to the main, google Doc.
English it, rather.
So, we have, let me find a way to hide this… I don't know, hopefully I won't leave the meeting. Okay, yeah.
So, we have this sheet that we said we should… we would encourage people to always have a variables tab, which will contain all the questions that are in this survey, then, communicates how we want to present them as a variable. You know, for example, now.
how large is the organization can be written as organization size, then how do you build your collector distribution can be built on collector, and so on, just like you can see in this document. Also, we want people to specify the kind of variables, because the type of variables you have will inform the kind of analysis you will do.
And, additionally, there is a comment here that I have not worked on, which is we want to also add all the options, or let me see, options that are available for the respondents to fill. At the point of the survey, we want to hide it here, you know, we just find a way to blow it up, just like we have it in the plan, so that when you're analyzing, you won't really need to go back to the main survey to get a full glimpse of what you're doing.
Then afterwards, when the survey is done, we want to make sure we are showing the general analysis of each variable in an overview. So, currently, for the collector survey, what I presented right now is the collector deployment location. I'm not necessarily going to be going to the insights, because I believe this is the end user feed. When I'm presenting to the collector feed, then we can start talking about what I think about these insights, then they can as well agree or disagree with what I'm thinking about it.
Then, we just presented each of the questions. For example, we have the collector diploma location.
The organization… organization size.
We have the collector telemetry types.
than the top 10 industries. This is definitely a comment here that we are thinking of, you know, recommending to people to take out percentages that are less than 5, so that we don't need to reduce this insignificant set of industries. And this is also raising a point for us to probably revisit what we have in the current survey, questions to probably see, because the three surveys that I've analyzed so far now.
don't necessarily have a lot of other feeds apart from technology and finance. So maybe we need to recategorize that, but we'll probably raise that conversation in the PR later.
then, we have shown the Kubernetes, scenario, deployment scenarios, the same types, you know, quite a lot of that with different graphs. You have vendor, whether you're a vendor or not, and how you documentation.
unless you want me to, you know… I don't know if me not necessarily discussing the inside is okay, but if we want me to do that, I can do that, but I'm checking other things down on the schedule, and I think the right audience will read the hotel collector's feed, then hotel room production.
ECC.
Then afterwards, we want people to have access to the cross-tablation tab, where we ask the real questions that we think people want to see. So for this case, we say, does those organizations are essentially produced running by OpenTelemetry in production.
So, This is… I have… we don't want to talk about it here, unless we insist I do so. Then, there are other questions that… that says, does team types produce implement environments?
You know… And, which Kubernetes deployment scenario?
align with specific user skills. You know, there are processes that that were followed to achieve all this, and this will be documented in our analysis plan. We already have guidelines for everything.
just need to start dumping Victoria, like, infographics into them.
So, then afterwards, there is a particular part that I have not added at all in the analysis guide, which is the additional analysis that can be done, which is where you can try to see whether you can check some, causal inference. That has not been communicated here, but in most cases, a lot of people don't have the theoretical knowledge to analyze causal inference, so I would expect that people will do that less, but I would still like to communicate it, that it is possible, in case you have the skills to do… to do it.
So that's… that's it. I don't know if, there are other… there are some parts that you want me to talk in more details about, but we just wanted to present what the progress is like for the current, collector follow-up survey, and… and afterwards, so this will be presented to the hotel collector seed.
In the vein that they probably will have some more interesting questions. What do I mean? Because the questions I have asked here, I believe, might not necessarily be so exhaustive.
compared to what the, hotel collectors themselves will hacks. So, the aim is to use the current analysis as an entry point to telling them, look, this is what we've done.
However, we understand that we'll be the best person to ask the best questions that we'll try to find ourselves to, which we will not communicate in our guide. So we are going to use this to, speak to the tech collectors engineers.
days, and we will get more questions. We'll get to work on this particular part of the document together.
So that we can close the analysis out in the coming days as well.
**Dan Gomez Blanco** 14:49 That's good. So these, these correlations, or, like, these questions here so far have been, I guess, not coming from the collector maintainers themselves.
**Ernest Owojori** 14:59 It's not. Okay. No, it's just for me.
**Dan Gomez Blanco** 15:01 Yeah, no, that… I mean, but they're really good. I think I really… this is really good.
You know, seeing that, I quite like that, aspect of, like, yeah, does organization size infer, you know, can you infer the, or predict the… Different… different other questions. This is really good.
So, yeah.
Looks great, looks awesome.
**Ernest Owojori** 15:24 Thank you.
**Dan Gomez Blanco** 15:25 How would you, are you thinking of, like, So, like, providing guidance to be able to do this For other service, is that the idea? Yeah.
**Ernest Owojori** 15:37 Yes, yes, that's the idea. We already… we already have a document in progress for that.
**Dan Gomez Blanco** 15:44 Awesome.
That's cool.
**Ernest Owojori** 15:47 God.
**Andrej Kiripolsky** 15:49 And I think, Ernest, maybe, maybe you could share in the doc, in the, in the…
**Dan Gomez Blanco** 15:55 In the notes.
**Andrej Kiripolsky** 15:56 In the notes, yeah, I think that, like, it's quite well.
elaborate, I think, at this point, as a first draft, and I think it would be great if folks could take a look and provide.
**Ernest Owojori** 16:07 Oh.
**Andrej Kiripolsky** 16:08 like, some early feedback. I think there will be still a lot of, Yeah, a lot of changes, but… I think, yeah, the earlier you start providing feedback, the better, for sure.
**Ernest Owojori** 16:20 You mean this, right? You mean the main data analysis guide?
Yeah, I mean this one. I mean this one.
Okay, okay, okay.
No problem, I'll do that.
**Andrej Kiripolsky** 16:38 Cool.
**Ernest Owojori** 16:39 Right, I think.
**Dan Gomez Blanco** 16:42 Next topic, humans Avot Tale for KubeCon North America.
I need to get updated on a lot of things, so I'm not sure who's leading on this. But…
**Adriana Villela** 16:55 Yeah, so I put that one on the agenda, so I'm… I'm helping out on… in terms of a supporting role, because I won't be at CubeCon North America.
However.
We do need a little more movement on this. We need to send out, the, sign-up slots to the people that we have identified.
as, interviewees for Humans of Hotel.
ASAP, because Henrik had a number of slots available at his special little CNCF booth, but it looks like they've dwindled, so we need to… We need folks to reach out to, yeah.
To these folks.
To the attendees.
**Sophia Solomon** 17:42 Adriana.
I can reach out.
Perfect, and we need to make sure, also, we have the.
**Adriana Villela** 17:51 So we have, like, because I know, like, Reece had put together, on, on Slack, like, a… a kind of a running list of, of who's, who we're interviewing. If you could put together a doc as well, like, just a Google Doc for that, so that we have kind of a… central place for that, and then what their time slots are, so that we have more visibility into that, because I would hate for us to, Miss out on interviewing people because we've identified them, but then…
**Sophia Solomon** 18:22 Right.
**Adriana Villela** 18:22 out to them, and then poof!
**Sophia Solomon** 18:26 Yes, yes.
**Adriana Villela** 18:28 Perfect.
Yeah, and Dan, for your background, we are still continuing with the humans of OTEL, both the livestream and the, the interviews. So, Sophia and Reese will be on-site to do the interviews. Henrik is going to be supporting from a video production standpoint.
And we've identified for the livestream, Jacob Arana, and then Diana Todeea as our livestream guest. Nice. So, and that's happening on the… I want to say the Wednesday at… 2.30 Eastern.
So, the other thing we need to do also is to get the promos out for that as well.
**Sophia Solomon** 19:17 Can I ask what you mean by get promos out? Like, just like…
**Adriana Villela** 19:22 Oh, like, we need to, we need to create assets to promote the, the event.
So that, like, Henrik can create the, the links on… on, like, for YouTube and LinkedIn on… on Restream, I think?
I think that's how it works for… I'm not sure if it's the same way for the livestream, but that's something to double-check with him on, on our Slack channel.
Around that, but, yeah, we need to create some thumbnails.
For YouTube, and for, for, like, our social media promotions.
And I think usually… Reese, correct me if I'm wrong, we also do the, like, the countdown stuff for the… for the humans in both a livestream as well, right?
**Reese Lee** 20:10 Yes.
**Adriana Villela** 20:11 Yeah.
**Dan Gomez Blanco** 20:13 Cool.
**Adriana Villela** 20:13 Yeah, so those are, I think, the outstanding items.
**Dan Gomez Blanco** 20:19 Left for humans involved.
Obviously, we're gonna be creating, hotel… OpenTelemetry Live.
Event as well, right?
Yeah, yeah, yeah.
For the livestream, yeah, cool.
**Adriana Villela** 20:39 Yeah, yeah, like we've done for the past, I want to say, two KubeCons?
**Dan Gomez Blanco** 20:44 Yeah.
Cool, awesome.
Cool.
So, that would be Reese and Sophia, is that?
**Adriana Villela** 20:53 Iris and Sophia will be running the interviews.
**Dan Gomez Blanco** 20:57 Got it, okay.
**Andrej Kiripolsky** 20:57 Yeah, and I just wanted to ask, so Sophia mentioned that she can do the… reaching out, and regarding the promos, is there anyone who would like to do that, or who… Agreed to do that.
Just to make sure that… that… There is somebody.
**Adriana Villela** 21:15 Yeah, no, I agree. I know, like, Reese historically has done the thumbnails and whatnot in Canva. Reese, I'll put it out to you as to whether or not you have the cycles for that.
**Reese Lee** 21:26 Oh, yeah, yeah, I can… I'll… I'll put those together.
**Adriana Villela** 21:29 Cool, cool, cool. And then social media, typically we've had Victoria doing that, but again, like, Victoria, I'll leave it up to you on whether or not you have the cycles, and I… sorry, I didn't check to see if we were actually on the call.
**Andrej Kiripolsky** 21:42 I don't.
**Adriana Villela** 21:43 Victoria's not on the call. Yeah. So if there's anyone else who wants to queue up social media promos, that would be awesome as well, once we have the assets.
**Dan Gomez Blanco** 21:56 I mean, I could probably do it, but, like, that's probably… I've never… I know that I probably have access to Buffer, but, like.
**Adriana Villela** 22:03 I believe you should, I think I added you as an admin.
**Dan Gomez Blanco** 22:06 Cool.
**Adriana Villela** 22:06 You… you, Reece and I are admins on Buffer, so I… any of us can approve… Else from anyone else, and… And if you're not on Buffer and would like to be added, let me know.
**Dan Gomez Blanco** 22:18 I'm getting the emails, so I'm about on the.
**Adriana Villela** 22:20 Yeah, okay.
**Dan Gomez Blanco** 22:21 I think I've got access… I think the OpenTelemetry admin, the admin.opentelemetry.io account has access to it, so… Oh, okay. Even if I don't have personal access, I'll be able to access it.
**Adriana Villela** 22:32 Okay.
Cool.
**Dan Gomez Blanco** 22:34 But let me know, yeah, is there an issue for, like, whoever, like, you know, when you're ready, I guess, let me know, and I'll… I'll share the link.
**Adriana Villela** 22:41 Bye.
**Dan Gomez Blanco** 22:42 I think that should be.
Yeah.
**Adriana Villela** 22:44 Perfect. And Dan, I think… let me just double-check the Slack channel that I have… that I created for this, but I think you should hopefully be.
In the Slack channel for humans involved. Okay. Okay, cool, cool, cool. Yeah, so then, like, we're using that channel to communicate, with regards to any planning, so we can use that, like, whenever Whenever the assets are ready.
Whenever the schedule is up, like, let's… let's make sure we continue posting in there.
**Dan Gomez Blanco** 23:25 Alright, so I think we've got, yeah, we've got some next steps.
M… So, yeah, the next one is from you as well, Adrena. What are the plans for the next What's New in OTEL, right?
**Adriana Villela** 23:38 Oh, yes, yes, so.
**Dan Gomez Blanco** 23:41 And the question is, like, when? Is it November, December? To be honest, I'm not sure if November, like, people are gonna be, like, you know, with KubeCon and blah blah blah, it might be… That's the thing, right?
**Adriana Villela** 23:51 And we have this livestream going on as well, which, I know we've typically… branded it as Humans of Hotel Livestream, but I wonder, because the content is rather more in line with what's new in Hotel.
Should we just brand that as a What's New in OTO livestream, live from KubeCon?
**Dan Gomez Blanco** 24:11 Yep.
**Reese Lee** 24:13 That makes sense. And then, yeah, I can talk to the.
**Dan Gomez Blanco** 24:17 Yeah.
**Reese Lee** 24:18 Who is it? Diana and Jacob, and… Kind of let them know.
**Adriana Villela** 24:23 Yeah, yeah.
And obviously, like, because it's a livestream, live from CubeCon, like.
we don't expect any slides or anything. Like, I know, like, the slides were very, very minimal for… for the one we had this week, but I think for on-site at KubeCon, it probably… We don't want to make it extra work.
**Dan Gomez Blanco** 24:43 I mean, that's a good question. I think, should it… I know that you said, you know, should we tweak the format? How long is it normally the humans of Hotel at KubeCon?
Like, life… The live? Is it one hour?
**Adriana Villela** 25:00 Mark likes to keep stuff for about 40 minutes with, like, 20 minutes for Q&A, but the actual content, he never liked to keep it more than 40.
**Dan Gomez Blanco** 25:09 Right. Minutes?
**Adriana Villela** 25:10 So, yeah.
**Dan Gomez Blanco** 25:14 So I'm just thinking, like, yeah, that'll probably make sense.
for the, you know, what's new in Hotel, I think that the first one was, like, was good, probably to have it It was 1 hour, I think, total, was it?
**Adriana Villela** 25:25 Yeah, it was 1 hour total, yeah.
**Reese Lee** 25:27 Yeah, I think it ran a little bit longer than we expected, but it was good.
**Dan Gomez Blanco** 25:31 It was good, and there's a lot of music.
**Adriana Villela** 25:33 interaction.
**Dan Gomez Blanco** 25:33 I wasn't expecting, like, you know, severing or, Or Marilla to come up with, like, slides and everything, so that, yeah.
**Reese Lee** 25:41 Yeah, that was a… that was nice.
**Adriana Villela** 25:44 Oh, great.
**Dan Gomez Blanco** 25:48 M… Yeah, I don't know, like, if when I do it in December.
Depends who's… but I was just thinking of, like, maybe, like, trying something… Short term?
Yeah. Maybe, like, slights optional? Like, I don't know.
M…
**Adriana Villela** 26:07 I was thinking, like, if we do it in December.
**Dan Gomez Blanco** 26:10 And they decided, you know.
There is a GC election happening.
There may be new people as well in the GC.
That get elected.
There's also new people in the TC, so maybe, I don't know if that's, like… That would be a good idea.
**Adriana Villela** 26:27 Yeah.
I like that. Actually, it would be kind of nice to dig a little bit into the GC and TC, because I feel like it might still be a bit of a black box for some hotel community members.
**Dan Gomez Blanco** 26:38 Yep.
Yeah, that could be a… a good idea.
Maybe we can run it past, Yeah, the TC as well, or the new members, maybe they, yeah, fancy joining.
**Adriana Villela** 26:54 Yeah, that'd be awesome.
**Dan Gomez Blanco** 26:55 Without putting him on the spot, you know, I guess. No.
Cool.
So we should aim for something in December, then.
**Adriana Villela** 27:05 Yeah. Yes.
That's perfect.
**Dan Gomez Blanco** 27:09 No, I mean, like, if… I could… I could probably join as well.
Nice.
**Reese Lee** 27:14 Nice. Cool.
**Adriana Villela** 27:15 Yeah, that'd be awesome.
**Reese Lee** 27:16 It'd be like… it'd be fun to do a holiday-themed…
**Adriana Villela** 27:19 Mmm, yeah…
**Reese Lee** 27:21 I'll be jumping.
**Adriana Villela** 27:23 There you go.
**Dan Gomez Blanco** 27:25 Get your eggnog and your obligumpers. I'm feeling like it's… temperatures dropped here in Scotland this weekend, and I was like…
**Reese Lee** 27:33 Oh, interesting.
**Dan Gomez Blanco** 27:33 already.
**Adriana Villela** 27:36 Yeah, we've already…
**Reese Lee** 27:37 Yeah, same here.
Yeah, maybe our background can be, like, a crackling fire.
**Adriana Villela** 27:44 And, and ugly holiday sweaters.
Don't forget, very important.
**Dan Gomez Blanco** 27:51 Right, okay, I think we've got that covered, conscious of time. Cool. Do we…
**Adriana Villela** 27:56 And can someone just create an item in GitHub just to capture that, though, so we don't forget about it?
**Reese Lee** 28:06 Oh, yeah, yeah, and the SIG board?
**Adriana Villela** 28:09 Yeah, yeah, yeah, yeah.
**Reese Lee** 28:11 I will do that right now.
**Adriana Villela** 28:13 Oh, thank you.
**Dan Gomez Blanco** 28:14 trees.
Yeah, and then updates from running streams in the APAC region.
When it's any streams, like, any, like, it's like old tell in practice, or HotelMe?
Stream?
**Adriana Villela** 28:34 All of the above, any of the above. Even… even what's new in OTEL, like, it would be kind of nice to just have some representation from folks in APAC.
I know, like, after the What's New in OTEL stream, like, Reese, Henrik, Lisa, Marina, Severin, and I were talking about, like.
I think Lisa brought up one of the challenges is that, the folks in Japan, not a lot of them speak English, so finding English speakers in Japan to present has been challenging, so I'm wondering if also We can expand.
I know there's definitely an interest in having, like, a Japanese community presence, but I'm also wondering the interest of finding speakers, to expand outside of just Japan, so, like, looking for folks in India, Australia, China, etc, etc.
**Dan Gomez Blanco** 29:31 Yep.
**Lisa Jung** 29:32 Is there a feature?
in YouTube where it translates and just puts out, like, a closed caption in whatever language you choose? Or am I, like, hallucinating? Is there… is there something like that?
**Adriana Villela** 29:50 Huh.
**Lisa Jung** 29:52 Because, like, almost…
**Adriana Villela** 29:53 Are you thinking, like, a real time, or after the fact?
**Lisa Jung** 29:56 after the fact.
**Adriana Villela** 29:58 Hmm.
**Dan Gomez Blanco** 29:58 After, definitely, I mean, it's… I mean, if it's not automatic, it's easily… doable. If it's the, you know, the live transcript will be more difficult. I'm not sure.
**Lisa Jung** 30:09 Yeah.
**Adriana Villela** 30:09 Yeah…
**Lisa Jung** 30:11 We shouldn't have language to be the bottleneck, so we should do it in whatever language that is the easiest for the speakers and the moderators, and then…
**Adriana Villela** 30:20 super fair.
**Lisa Jung** 30:21 Availability should be, like.
after the fact, and just addressed through closed captioning or whatnot. I mean, there's gotta be… right? Yeah, like AI, too.
**Adriana Villela** 30:32 I know, right? I do feel like we're… we're modern enough that this stuff could be available.
**Lisa Jung** 30:38 Totally, yeah.
Yeah.
**Adriana Villela** 30:46 Is that something you can look into, maybe?
**Lisa Jung** 30:48 Yeah.
**Adriana Villela** 30:49 Cool, cool.
**Lisa Jung** 30:50 Absolutely. Yeah, and then, I know Andre has given me some, like, leads to go on. I've been looking at, like, X to see if anybody has spoken about OTEL.
In Japan, or, like, APAC region, but if you have any suggestions, let us know, because right now, like, finding the speakers is, like, the only thing that's getting in the way right now.
**Dan Gomez Blanco** 31:19 I don't end.
**Adriana Villela** 31:20 You know, we can, we can take to LinkedIn as well, and just post on the hotel socials, and say, hey, we're looking for APAC speakers.
Because I do feel like we get… we get good traction on LinkedIn.
**Lisa Jung** 31:34 Yeah… how about… you know what, I'll work with Yoshi to come up with, like, a… I mean, would you mind if it's, like, in Japanese?
**Adriana Villela** 31:43 Oh, let's do it, yeah.
**Lisa Jung** 31:46 And then see… Like, who comes out?
**Adriana Villela** 31:50 Yeah, I think it would be nice, actually, because then it'll also signal, like, hey, we are… we are inclusive, we're… we're working on We are working on more inclusivity, so, language-wise and whatnot, so… yeah.
**Lisa Jung** 32:02 Okay, so I'll create an issue, and then, come up with some drafts, and then we can go from there.
**Dan Gomez Blanco** 32:08 Sounds good.
**Lisa Jung** 32:08 Yeah, and I'll also research the AI tools to see if there are, like, AI translation closed caption tools.
**Adriana Villela** 32:16 Amazing.
**Dan Gomez Blanco** 32:17 Cool.
**Lisa Jung** 32:18 Goku?
**Dan Gomez Blanco** 32:20 And, also linked to the next topic, which is, you know, the three potential speakers that, Adriana was saying. If these are EMEA speakers, or European… we can also make it, you know, we can also, like, have a session in the morning in Europe, so that, you know, basically is… a, you know, friendly… friendly time for anyone in APAC as well, right?
**Adriana Villela** 32:45 Yes, that's true.
That is a good idea.
Yeah, I know two of them… I want to say two of them are EMEA, for sure.
The one guy who's Brazilian, I don't know where he lives.
I don't know if he lives in Europe or in Brazil, or neither.
**Dan Gomez Blanco** 33:08 Oh, neither.
Cool.
I just do, to… yeah.
to link to the next topic, I guess.
So we've got a few folks, then. So… If we've caught, like, I… Are those for, like…
**Adriana Villela** 33:25 Hotel me, hotel in practice… Yeah, hotel me, hotel, and practice.
I always try to hustle and get them for both, but it'll be at least one or the other.
**Dan Gomez Blanco** 33:38 Okay.
**Andrej Kiripolsky** 33:43 I had a comment there, not sure, like, but if… If you have anything else to add, feel free, and I will just mention later.
**Adriana Villela** 33:52 No, no part.
**Andrej Kiripolsky** 33:53 So I talked to, a Prometheus maintainer, Arv, And, so Prometheus folks.
Would like to socialize better the ways how, like, How they envision, Prometheus users to ingest, hotel data, because apparently the most popular way how to do that… is really quite, cumbersome, and people have a hard time with that. This is basically what Victoria's research was, was about.
that she conducted through her mentorship. And, yeah, folks said that, like, hey, we have better ways, but probably people just don't know about it. And I mentioned that perhaps he could join hotel in practice, and mentioned that, and I… but I wanted to ask you folks if that's… if that's okay. Like, Prometheus is a CNCF project, so not sure if, like, how do we… how do we look at them? Is it… is it from the… from the… Hotel perspective, is it a vendor, or is it okay, or…
**Dan Gomez Blanco** 35:06 No, I think it would be… I think it would be awesome to have, like, someone from Prometheus to do, like, hotel in practice or something like that, but it sounds like, you know, what you're talking about would be more… towards that hotel in practice type of session, right?
**Adriana Villela** 35:20 I could even envision, also, to milk this further, as part of the What's New in OTEL, to have something around, like, OTEL-Prometheus interoperability.
Because we do have, like, a huge Prometheus, community, so I'm sure folks would appreciate that as well.
**Dan Gomez Blanco** 35:41 Well, if you're convinced, so David, Ashport, that is…
**Adriana Villela** 35:45 Yes.
**Dan Gomez Blanco** 35:46 new in the TC is also in that Prometheus interpreter.
He's one of the sec leads, so, as well.
So… That would be a good one.
**Andrej Kiripolsky** 35:58 Perfect. So, I'll let Arv know, and I'll try to talk to Prometheus folks about, like, who would be… who would like to… who would like to… talk about the interoperability part. But yeah, David would be, for sure, a good candidate.
**Adriana Villela** 36:13 That's great, and let's, let's throw out some, let's throw out some dates as well. Let's look at… because no one, like, of the people I talk to, no one has, like, fully committed yet. Everything's kind of wishy-washy, so let's throw out some dates, in, like, November, December, January.
**Dan Gomez Blanco** 36:33 Yep.
**Adriana Villela** 36:33 That could work with them, so that we can try to nail… nail something down for the hotel and practice.
**Andrej Kiripolsky** 36:41 Okay, okay. I know, well…
**Adriana Villela** 36:44 We just came up with this idea, like, 2 days ago, so I don't… Yeah, yeah, no worries, no worries.
**Andrej Kiripolsky** 36:48 I've mentioned that he doesn't have anything prepared, so I think it would be good to give him at least a couple of.
**Adriana Villela** 36:54 Yeah, yeah, yeah, whatever, like, whatever they're comfortable with.
Yeah, just feel free to work with him on some potential dates, and then we can circle back with Henrik and see how that fits his schedule as well.
**Andrej Kiripolsky** 37:06 Sounded good.
**Adriana Villela** 37:07 Cool. Yay!
**Dan Gomez Blanco** 37:17 Well, next topic, we've got from Andre.
**Andrej Kiripolsky** 37:22 Yes.
Topic? Yeah. So… the PR… actually, when I had it in my notes, I stopped calling it… like, I didn't know how to call it, so it was, for me, just, like, the long, delayed task, because I think I assigned myself to the task, like, in March.
But now it's done, and there is a big refresh of end-user resources page, OpenTelemetry.io, and why I'm mentioning it, it's not over. And I wanted to ask you folks, like, now it's, Like, the text is new?
and the structure is new, but I think now it's the time to make it look pretty. Now is the time to add images, and to, like, play with… I don't know, like, interface elements, I can imagine, like, having buttons there or something like that. So I just wanted to mention that if anyone is interested and would like to make this type of contribution, I created an issue for it, and yeah, so feel free to… To grab it and, make the page even prettier.
So, that's… That's it.
And nobody has to commit right now. I mean, just think about it, take a look at the issue, and yeah, if you feel like it… like, no need to do it and then actually do the work 6 months later, it's terrible.
And, yeah, I have the next one as well.
That's about, So, yeah, I was… I was going through the, through the issues, and there are two issues opened for…
**Dan Gomez Blanco** 39:05 Let me share my screen.
**Andrej Kiripolsky** 39:07 in one event, I think Rhys just closed one of ours.
**Reese Lee** 39:11 Oh, yeah.
**Andrej Kiripolsky** 39:13 I did disclose one. That's right.
**Dan Gomez Blanco** 39:18 Sorry?
So the first one, find speakers for the first episode of what… that's already been closed, so that's good.
**Andrej Kiripolsky** 39:25 Cool. Cool, cool, cool. Yeah, yeah. And, I guess, like, the second one, I guess it's still… there might be still something to do, but… yeah, since the session already happened, I just wanted to bring it up that… Yeah, yeah.
**Dan Gomez Blanco** 39:39 do we… I guess the… creating the to-do template, like, in that second one, that would be… Beautiful.
Or like, issue template.
**Andrej Kiripolsky** 39:53 Where is it?
**Dan Gomez Blanco** 39:54 So I'm just looking at the… I'm looking at the… I'm not looking at the screen that… I'm looking at the… Issue that was linked.
There's one.
**Andrej Kiripolsky** 40:02 Yeah, I cannot find it, so it's good that you're not looking at the screen, because it's not there. Anyway, yeah, so if you can just click on the links, that would be better.
Yeah, that's it, that's it. Just, like, heads up that there are two issues that are done, and it's awesome.
**Dan Gomez Blanco** 40:18 Was the idea to, like… write a blog post about what's new in Hotel? Or… or just… Have the session.
**Reese Lee** 40:26 I think that was an idea that we floated around, And I meant to reach out to Severin and Marlia, but I haven't yet.
Like, I still think it… Should… Shouldn't be too hard, because we can just use a transcript and, you know, write something from it, but…
**Dan Gomez Blanco** 40:45 True.
Just for information, I'm not sure if, I mean… This doesn't mean that we don't do it.
Mmm… But there's one thing that we… we were thinking about doing from the… from the TC and the GC… On a maybe quarterly basis, rather than a monthly basis, to do a… like a… almost like a roadmap review, blog post. Nice! Something like that. So I don't know if that, you know, if that sort of covers a little bit of that, you know, what's new and hotel.
I don't know, maybe not. Maybe it's better to, like… it's completely different, because I… you did talk about some things that will not be in that roadmap.
review blog posts, right? Like, Hotel Unplugged, or the elections, or things like that.
So… I'm just convincing myself that what I said was not a good idea.
So I… But, yeah, no, I think that's… I think a blog… a quick blog post is probably quite… quite good.
**Reese Lee** 41:46 Okay.
**Adriana Villela** 41:46 I wonder if we can cheat a little bit and do kind of what we do for Humans of Votel and just post the transcripts?
**Dan Gomez Blanco** 41:53 Yeah, just…
**Adriana Villela** 41:54 And then, like, 5 bullet points that highlight, like, the main… the main takeaways.
So that's… that's one. Another is to, like, almost do a blog post that's newsletter style, that, like, links to the things that were discussed.
in the What's New in Noel, or just, like, draw people's attention. Because there's also, like, I've noticed there's always a no-tel blog post of, like, this thing is new, and that thing is new, and that came out, and so having, like, a digest blog post, you know, that summarized, that just lists, like, hey, check these things out.
That could be another thing to consider.
**Dan Gomez Blanco** 42:33 Yep.
**Reese Lee** 42:37 Okay.
**Dan Gomez Blanco** 42:47 Alright.
I think I've got a few topics now as well.
Is that… are we okay with that, or… To move on?
**Reese Lee** 42:56 Yeah, I'll take a stab at it.
**Dan Gomez Blanco** 42:58 Awesome.
Alright, so, I'll share my screen first. For anyone that doesn't know what Renovate does, and probably a bit of context as well on, what we're getting, if you've seen PRs here at that.
I guess, you know, we've got a few PRs. I've been merging some of them, but… So these are PRsuit bump versions of libraries, and the script that we got a donation for, so we've got video transcripts, right?
And here we've got, requirements.txt, and, you know, basically this script will use these libraries, and we've got, yeah, renovate will just run on a cadence, on a specified cadence, and then… Send updates to update these libraries, right?
If we don't update them, then we get some security.
Think… To be fair, like, it's not like we are providing this as a software for other people to, like, you know, run in their own… environments, it's more like tooling for us, but, you know, anyway, it's probably a good practice. And I was thinking.
I've been merging the ones that are patch versions.
And then I was gonna merge the ones that are, like, Major version bumps.
But I'm, less… Yeah, so this is going, you know, quite low version, so I'm like, if I do this, will it break the complete, you know, will it break the script?
Don't really want to write the script.
And there are no unit tests here to actually test, you know, even, like, the most basic stuff.
So, what I was thinking is, like, it would be cool, and I think I could give it a stab, but I've been… I wouldn't be able to do it before KubeCon.
And to create just some simple unit tests, and… You know, something that can be run.
And CI, so, like, when, actually, when to get a PR, that is… Created, you have a GitHub Action that gets triggered, and then have that, basically.
As a validation that when we touch these files.
We're not breaking something, and we can just merge the upgrades.
Does that sound like… I mean, I can probably create an issue for this. I should probably create an issue for this.
And then someone… yeah. Either… if someone wants to take it, feel free. If not, I'll probably… I will do it, but it'll take me a while.
But I guess I've explained the issue, more or less.
**Victoria Nduka** 45:30 I was going to ask… How much… how much technical knowledge you need to… is it… is it, like, a good first issue?
**Dan Gomez Blanco** 45:41 Could be a good.
**Victoria Nduka** 45:41 Boofest.
**Dan Gomez Blanco** 45:42 Yeah, I think it could be. Also, like, you know, the fact that we've got requirements.txt, you know, you get, like, the… every single library here that's upgraded.
when, like… One could potentially argue that if you had a setup.py.
You only have the libraries that you depend on, not the transitive dependencies, and then that's the ones that you update?
But I guess, you know, we can explain that in an issue. Basically, the whole idea is this script here has dependencies, we need to update the dependencies.
every once in a while, how do we make that in a way that is… Easy, and we don't break it. And for that, we need… Like… The dependencies to be… defined in a way that is easier for… that can renovate, can upgrade. And also, some unit tests that allow us to… Let me ensure that we can merge it without… Having to also run it manually. Ensure that, you know, we don't… break him.
At least not break it super badly.
**Victoria Nduka** 46:46 Okay. I asked because I was wondering if… If it's… it could be a way to get more contributors, maybe we could.
**Dan Gomez Blanco** 46:55 I mean, I think that would be a… it would be a…
**Victoria Nduka** 46:56 Confusionists.
**Dan Gomez Blanco** 46:57 It would be a good frustration, yeah, I think so.
**Victoria Nduka** 47:00 Okay.
**Dan Gomez Blanco** 47:02 Yep.
I will mark it as such. I will create, if you… yeah, I'll create an issue.
For this, and then Market has good fresh tissue.
**Victoria Nduka** 47:12 Okay.
**Dan Gomez Blanco** 47:15 Cool.
Another one.
Hotel, this is probably the first time you've heard of this. Hotel Blueprints. That has been… so just a bit of context, I don't know if anyone's heard about… Well, you've probably heard of that. OpenTelemetry, we're running for graduation, and in a… In CNCF, as part of our graduation process, there is a… adopter feedback or adopter interviews. There was some feedback that was given back by adopters, and some recommendations that we… and these are public, I can link them in here. There were some recommendations from the CNCF, Technical Oversights Committee… oh, oversight… Oversight Committee.
on, yeah, things that we could improve on as a project. Some relate to… How we communicate stability of different components, some relate to the… I don't know, release life cycles, and so on.
And then… some are related to the way that end users… adopt OpenTelemetry, or the way that they, in a way, install OpenTelemetry.
And this, basically one of the recommendations is something that I think I spoke about with somebody else.
Before, in the end user, which is the concept of blueprints.
So, I'm… Blueprints as a way to, say, take different environments and take some… best practices that are recommended from the projects to adopt hotel, from the configuration of the SDK, to perhaps, like, you know.
architecture patterns and deployment patterns for… for collectors and so on. I think in the… currently in the collector side of things, there is, like, an effort to improve the collector deployment patterns part of the documentation.
So that doesn't change. That will… that work that's currently been doing collectors will continue. This… this sort of, like, hotel blueprints will… would sort of, like, sit at a higher level.
Of, like, looking at Hotel.
For different types of environments, like, for example, doing, like, Kubernetes, or… or deploying in… for hotel for infrastructure monitoring, or all the use cases, I guess, that we can think of.
And they're having, sort of, like, a formula, like a… Yeah, a little bit of a guided way of… doing it, follow best practices. Now, I think for this to be successful, and this is what I wanted to share here, is that I would love to get end users involved.
And, something that Alolita has been doing in the CNCF end-user Tab.
Is, a working group.
is reference architectures.
general, same CF, reference architectures, but I think this would be quite good if we could get End users involved.
to share.
Some of our high-level reference architectures that they have deployed, in particular environments where they've deployed hotel at scale.
And then we can take those… And… Yeah, basically write blueprints.
That can link to those reference architectures, that can link to other types of documentation, and almost, like.
A little bit of, A journey to adopt hotel, right?
In different environments.
So… first question… so basically what I'm thinking is, like, to raise a project?
Project proposal within the community.
I will be leading this. I'm a volunteer to lead this.
Not alone.
Maybe, I don't know, maybe somewhere else. So basically, what I want to get is, like, more people to join, and then end users or not.
And hopefully people that are closer to the field.
And, yeah, that can help us to… To put these down, and then to… Have a bit more of a… community around, hotel adoption.
M…
**Reese Lee** 51:38 Yeah, what kind of, Well, I guess I'll wait until you create the project and see what kind of work you need help with.
**Dan Gomez Blanco** 51:47 Yeah, so I guess, you know, the first… the thing that I will definitely need is, like, first will be end users to… to know about this, and to… to… We need to raise awareness that we want to do this.
And that will be the first step, right? We want to… We want end users to come in and tell us about their Their infrastructure, and the… and ideally, like, you know.
In a standard way, or like… not standard, but in a… In a given format.
As in, like, you know, we… we give them a little bit of guidance, like, tell us about, I don't know.
How do you configure the SDK? How do you, deploy collectors? What environment do you do this in? And then take a specific Use case, right?
**Reese Lee** 52:34 Gotcha, okay.
**Dan Gomez Blanco** 52:35 I think that's the idea. Then after that, I think we… when we've got… I don't know, 2 or 3 reference architectures, we can start to… turn that into some reusable patterns, I think that's the idea. I mean, maybe reference architectures will contain things That are not applicable to everybody, or that we see that they're maybe too specific.
And then we can abstract that a little bit into a blueprint.
That would be more high level, but then linked to specific reference architectures to backhit with evidence that people are using this in the field, right?
Andre?
**Andrej Kiripolsky** 53:10 I wanted to ask, like, in OTELMe, we are asking, like, kind of similar questions. These are sessions with end users, and I think there are a lot of questions about, like, how they set up OTEL.
would it perhaps be possible to just, like, elaborate more on, oh, tell me, have it perhaps, like, a more… Like, yeah, update the questions, and maybe go deeper a little bit, and this way we would have, like, two things done at the same time? Just an idea.
**Dan Gomez Blanco** 53:40 No, that's a good idea. I think, yeah.
I think I know tell me… Yeah, but I do think… yeah, imagine, like, if you had that, but, like, in a structured way of saying, this is how I deploy it.
I mean, we could probably go back to some of the sessions I've done with HotelMe and try to extract some common patterns from that, to be honest. That would be… wouldn't be a bad idea.
I think.
M… Yeah, this will take time. I mean, it's not gonna be, like… I don't expect this to take years either, but, like, I think that… Getting end users to… be comfortable as well presenting that? I guess that's the thing, like, you know, we need to put a name to it.
Well, that, well, we don't need to, but it would be good to put a name, too.
to it. I'll link the… I'll search, let me see if I search… And… User… no, CNCF Reference Architectures.
I mean, we can even pick some from here. So that has some… There we go.
Man, there's only two, actually.
Alolita said that she would also be… Happy to… Yeah, to tell us more about what the end-user SEC is doing.
or the end user tap is doing in CNCF, and then… because they've been also trying to get… Companies to provide their… reference architecture is?
So something similar to that.
That was the first step, I think.
And then we can go into providing the blueprints.
I guess my thinking is, like, if we think of blueprints without being backed by end users, it might… not… I don't know. We might be missing something, right? I do think the end user aspect is quite important.
M…
**Reese Lee** 56:02 Yeah, no, that makes sense.
**Dan Gomez Blanco** 56:12 Any questions on this? Or, like… I mean, I'll probably create a project proposal next week, and then… In that project proposal, you can just… comment as well, to clarify what we're trying to do, and then, yeah, we can… we can have that discussion. I'll be able to… I'll share it, definitely, within the… And… second user.
**Reese Lee** 56:33 Okay, sounds good.
**Dan Gomez Blanco** 56:35 I think this could be good. I mean, it's something that I've been wanting to do for a while, and now, I guess that… the TOC came back and said, this was a really good idea, and then… well, I mean, not that they told me it was a really good idea. They said, like, this is something you should do, and I was like, well, we're already thinking about that, so…
**Reese Lee** 56:52 No, that's awesome, yeah.
**Dan Gomez Blanco** 56:57 Awesome.
Alright, I think we've got 4 minutes left. I just wanted to say, hotel unplugged.
Don't know if you've seen this, but… tell your mates.
Especially for people that are coming to 4STEM already, or that are… Europe, paste.
**Lisa Jung** 57:18 I have one more thing to add on that. So, the organizers for OTEL Unplugged asked our help to promote it via our social promo channels.
So, they're gonna get a draft ready to be reviewed by both, Communication SIG and End User SIG. So, once they get that draft ready, I'll create an issue and then tag all of you for your review.
**Dan Gomez Blanco** 57:42 Nice.
Did you all know that 4STEM happens in a weekend? There's a conference over the weekend?
I didn't know that.
**Lisa Jung** 57:51 Russell.
**Dan Gomez Blanco** 57:54 That is new to me.
**Reese Lee** 57:57 Yeah.
I… yeah, that's interesting.
**Victoria Nduka** 58:04 I'm sorry, like, it's weird that the conference is happening over the weekend.
**Dan Gomez Blanco** 58:08 Yeah.
**Victoria Nduka** 58:10 That's normal for us.
Often, if you're the, if you're at a conference, during… Only, on the workday.
**Dan Gomez Blanco** 58:20 You're not very likely to get a lot of attendees, because then they'll be at work.
**Victoria Nduka** 58:25 in… in… I'm talking about in the INA area.
So he's interesting to Brando, that's For you guys is different.
**Dan Gomez Blanco** 58:33 yet.
**Victoria Nduka** 58:35 Perfect, guys.
**Dan Gomez Blanco** 58:36 I consider them work, so the weekends I don't work.
**Victoria Nduka** 58:39 Oh.
**Dan Gomez Blanco** 58:41 But, you know, I understand why, I think, as well, they do it, so…
**Victoria Nduka** 58:46 Right?
**Dan Gomez Blanco** 58:48 Cool. Alright. We're out of time.
Any other topics?
**Reese Lee** 58:57 ones.
**Dan Gomez Blanco** 58:58 Going twice.
Awesome. Right, we'll see you in a couple of weeks, then.
**Reese Lee** 59:04 Thank you, everybody!
**Dan Gomez Blanco** 59:05 To you, boy.
**Andrej Kiripolsky** 59:06 Bye-bye.
**Ernest Owojori** 59:08 Bye.
**Adriana Villela** 59:10 I…
