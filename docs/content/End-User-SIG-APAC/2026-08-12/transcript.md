SIG: End-User SIG (APAC)
Date: 2026-08-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Dhruv Ahuja** 02:42 Hello!
**Ashwini Manoj** 02:48 Hi.
Can you hear me?
**Dhruv Ahuja** 02:51 Yes, yes, I can hear you.
**Ashwini Manoj** 02:53 I'm the word.
This is my first time attending.
**Dhruv Ahuja** 02:59 Oh, nice.
**Ashwini Manoj** 03:00 Yum.
**Dhruv Ahuja** 03:02 Welcome.
Okay.
**Ashwini Manoj** 03:04 Thank you.
**Dhruv Ahuja** 03:06 Oliver is here, let me check if some other folks are joining.
**Ashwini Manoj** 03:11 Got it.
**Dhruv Ahuja** 03:36 Yeah, most likely Andre will be… will be here. He's the maintainer.
And Yoshi is also heading this, APAC call, but he's off this week.
**Ashwini Manoj** 03:51 Okay, got it.
So, Dhruv, what do you do here?
**Dhruv Ahuja** 04:19 So I started about 2 months back, but I've been quite active. And mainly I've been helping… so I recently helped out with the survey, and then I've also been picking up other, minor tasks or contextual tasks as they come along.
So, I'm primarily… yeah, so the biggest, thing I did is just, was the, there was a survey that we ran recently, and I helped conduct analysis for the same. Because when I joined, the survey was already done, and the data was available, but the analysis hadn't yet been started.
So I took that up.
**Ashwini Manoj** 04:59 Oh, nice.
**Dhruv Ahuja** 05:01 Yes, and now, so Andrej has written a blog post about it, a blog post draft, and there's an ongoing discussion on the same.
So I suppose once it's done, we'll go ahead and make it live.
**Ashwini Manoj** 05:14 Got it, yeah, thanks for that.
**Dhruv Ahuja** 05:18 Yeah.
And, what about you? Would you like to tell a bit about yourself?
**Ashwini Manoj** 05:25 Oh, yeah.
**Dhruv Ahuja** 05:25 deal this one?
**Ashwini Manoj** 05:27 So, I'm Ashwini, I'm from Bangalore.
And I work as a software engineer here. I have about 9 years of experience now.
Yeah, and I've been in the observability world for some time, open telemetry in the last 6-7 months.
So, yeah, I've been, you know, just been a consumer of content and everything. I thought I'll join in today to be part of… The group, actually.
So, yeah, my… I work in CrossFit. It's a service-based company here in Bangalore.
And you're focusing on observability.
**Dhruv Ahuja** 06:14 Oh, nice.
I think Andre will love it. Oh, you're in a car.
**Andrej Kiripolsky** 06:20 Hi, everyone. I'm super sorry, I joined the wrong meeting. Like, we were changing meeting links, and I was actually supposed to be the one who was, like, making sure that people are not joining the wrong one, and I joined the wrong one, so… my apologies.
**Ashwini Manoj** 06:35 That's okay, I guess you made sure nobody else is there, so…
**Andrej Kiripolsky** 06:39 Yeah, that's for sure. Yeah, nobody was there.
**Dhruv Ahuja** 06:41 Yeah.
**Andrej Kiripolsky** 06:42 It's just me. Yeah, yeah.
Yeah, good, yeah. Sorry for letting you wait. Yeah, shall we get started?
I guess… Yep. So, I see that, Ashwini is new, I guess? Have you joined the meeting before? No.
**Ashwini Manoj** 07:02 No.
**Andrej Kiripolsky** 07:02 Let's start with a quick round of intros, and then we can just go through the agenda that we have for today.
How does that sound?
**Ashwini Manoj** 07:10 It's called?
**Andrej Kiripolsky** 07:11 Okay.
**Dhruv Ahuja** 07:11 Yeah.
**Andrej Kiripolsky** 07:12 My name is Andrej, I'm a user… End-User SIG.
maintainer in OpenTelemetry community.
And, yeah, I help run these, APEC-friendly SIG Meetings. I'm based in the Czech Republic, now I'm on a vacation, kinda.
In, in Slovakia, so that's why I don't have, like, a proper office, and I work from a car.
But… Yeah, other than that, I'm a user researcher at Grafana Labs, and I somehow also am involved also with the Prometheus community as well.
So, that's… that's about it from my side.
Dhruv, do you want to go next?
**Dhruv Ahuja** 07:53 Yeah, actually, I've… you were just talking about it, so I've given my intro, but yeah, let me reiterate again. So, I… yeah, I didn't actually tell, what… what work I do, so I am a Devil at Cygnos, which is an hotel vendor, a startup hotel vendor.
And basically, I got involved because I liked observability even before I joined my current company, so… but it was, like, at an amateur level, so… But I had integrated some basic setup for the previous company. I liked the idea of, like, just seeing the number of errors go down, seeing how traces look.
And, like, the waterfall it forms, and then how that is really different than just blindly grapping for logs. So I got interested into that, and then when I got a chance to get into observability, I did. And then I started getting into the hotel community, and… well, what do you know, it's so welcoming, because I wouldn't have thought That it would be this, like, comfortable to be here.
If you look at some of the other dev communities, you could see that, okay, people, they are, like, some grizzly veterans who kind of… and you have to go through these rites of passages, you could say, that you have to really fight to get attention, but that's not the case here. Everything is super organized, and… things are, like, people are helpful, and the work here is interesting as well. So, kind of like a cross-collaborative effort.
So I'm active in two SIG, this and the contributor experience, and both have some overlap. So I'm often quoting what the end-user SIG does in the other SIG, the other group, and what they do here often.
So it's quite fun, and I think I'm learning a lot about how the community is shaped, and how they are working, and how things are progressing.
So, nice to be a part of it, and yeah, hoping to grow as well. So, we are also having discussions around how I can grow. So, we had such discussions, I believe, a couple of times. We are working towards that end, personally.
**Ashwini Manoj** 09:56 Sounds great.
**Andrej Kiripolsky** 10:00 Yeah, ashwinn, do you want to go next?
**Ashwini Manoj** 10:04 Yeah, I can go next. So, I'm Ashwini, I'm from Bangalore. I work in a a company called Infraspec. We have been exploring availability in the past few projects that we've been working on. Signos was something that I integrated in my last client. So, so what we did was we had open telemetric collectors, streaming to SIGNOS as a backend.
So, that is where I got started with OpenTerremetry, and it's been really interesting exploring selector, collector config, and I was like, oh, it's… it's not as, like, I mean, I know there's, like, open source projects and demos and all of that, but it still took some, you know, exploration to figure out what I really wanted. So now we have, so there have been other clients that we are working with where we are also, like, you know, setting up observability stack for them, or improving what they already have.
So, that's where I got involved, and I thought I'll join in on the OpenGenevity group as well, because it's very relevant to what I'm doing, and it's interesting to see all the blog posts. I recently started following those as well.
So, yeah, I thought I'll join in and see what… where I can contribute, and… Yeah, that's… that's how that is. I have about 9 years of experience now. I work as a software engineer, here at Represpect. So, we are a service-based company, so yeah, we work with clients and Right now, we're focusing on observable.
**Andrej Kiripolsky** 11:42 Nice, nice, thank you.
Oil or Victoria, do you want to go next?
**Victoria Nduka** 11:49 Yeah.
Sorry, sorry that I didn't give you tape.
I think I… I just woke up.
I don't know if you can tell why this was called.
Good morning, everyone. Good morning.
**Ashwini Manoj** 12:03 Good funding.
**Victoria Nduka** 12:03 Good morning.
And Victoria Nduka.
I'm based in Lagos, Nigeria.
UX designer turned cloud engineer, who I currently work as a technical support intern at Geometrics.
I started contributing to Open telemetry.
a little over a year ago, I got involved through the Linux Foundation mentorship.
And, yeah, the… Sorry.
Sorry, don't explain my clock.
And… yeah, like, like, Dhruv… Can't hear me.
Damn.
**Ashwini Manoj** 12:51 We… yes, fitting here.
**Dhruv Ahuja** 12:53 this weekend.
**Victoria Nduka** 12:55 Okay, because I'm using my phone as a hotspot, and I'm receiving a call right now, so I think… I'm hoping it's not interrupting the network.
So, like Dhruv said, the community has been really fun and interesting to contribute to, and I've come from being just a contributor to being an approver for the End-User C.
And I contribute primarily to the energies at SIG, and sometimes to docs as well.
So… Yeah.
Yeah, yeah, yeah.
So that's… that's it about me. And welcome, Ashwini. Nice to have you.
**Ashwini Manoj** 13:34 Thank you for that.
**Oliver Bassett** 13:39 Hi, so, Oliver, this is my second meeting. I missed one in between, I think, but, I'm a massive fan of OTEL, and a big user of it at our company.
So… I'm still figuring out how to get involved, but I thought that the best thing to do is, like, start joining meetings that are close, and then start… paying attention and seeing what things I can help with when I've got the cycles to do it, so… So, welcome.
**Ashwini Manoj** 14:13 And follow your footsteps.
**Andrej Kiripolsky** 14:17 Amazing, thank you, everyone. As usual, like, you folks who've been to a couple of these, I will just give a quick description of how this meeting works, and why… what is End-User SIG. So, End-User SIG is one of many, like, SIGs or working groups in OpenTelemetry, and we are… a cross-cutting SIG. It means that we don't focus on, like, specific part of the project, but we are trying to be relevant for all the parts of the project. We are trying to help the other, SIGs, like, for example, SDK SIG, or SIGs, or Collector SIG, and these ones, with collecting feedback from end users.
So that's our main mission.
And, we do 3 types of things, so we either, mostly it's either surveys. We run surveys with our end users and analyze results and write blog posts, we'll talk about it shortly, or we do live streams.
Where we ask.
people from the community. It can be either end users, or it can be maintainers, or it can be companies that are… or contributors. We give them space to share what is their setup, how they are working on hotel, and so on. These streams are on YouTube and are livestreamed.
Or, the third thing that we do, and it's, like, a big undertaking, it's blueprints and reference architectures.
it's, like, documenting how hotel is supposed to be used, and how it is actually being used out there in the wild. So these are the main three types of work that we do. At the same time.
We are also trying to be very welcoming and open for any initiatives that folks who are joining have, so if you have any ideas about what would you like to contribute, and it doesn't fit into any of these buckets, still, it's totally fine, and we are happy to, yeah, provide you with a platform to contribute.
Oh… Yeah, also, we are happy to just direct you to ever.
Oh… you might be more inter… or, like, what part of hotel you might be more interested in, we can tell you where to… where to go to get feedback, to get involved.
not… yeah, so it doesn't have to be necessarily just… just, End-Us SIG, but we… we… especially for this APEC, for APEC, meetings, we are trying to be this starting point, where we, like, channel people to… to different parts of the hotel.
Afterwards.
Yeah.
Thank you very much. Also, as folks mentioned, Ashwini, we're glad to have you here. Welcome. And, I guess we can get started with the agenda, and then… And we can… yeah, I think we have just a couple of points there.
And we can… we can continue with… with whatever discussion or just chat afterwards.
Sue.
The first thing is our blog post for OpenTelemetry Prometheus Interoperability Survey.
This is a survey that we ran, like, 2 or 3 months ago.
We originally started at KubeCon Europe, but eventually switched to, like, online, gathering responses.
And, Yeah, Dhruv… Dhruv did a lot of work on analyzing this, so he did all the, like, massaging of the data, and I eventually, got to writing a blog post. So right now.
No, this is not it.
Where is it? Sorry? Yeah.
**Dhruv Ahuja** 18:08 Findings tab, I believe.
**Andrej Kiripolsky** 18:10 Yeah, findings tab, yeah, yeah, yeah, yeah, cool. So, the blog post… is here. Thanks, Dhruv for providing your feedback. I reviewed a couple of things, and I, like, by incorporating most of the things that you, that you, mentioned.
And, one thing that I am waiting for is to get feedback from Arthur Sense, who is a Prometheus maintainer, and who came up with the idea to run this survey.
There are certain nuances about How we report maintainers.
And just in general, you know, he's a domain expert in Prometheus land, so I want to get his thumbs up.
this is something that I would love to get today, actually, because there should be a Prometheus meeting today.
So I'd like to… I'd like to mention it to him there.
End-U.
It's not that much text. Also, it's like 10 pages, so it's not short either, but if anyone is interested in providing feedback, it would be very… Very thankful for that.
It's not a big deal, also, so… yeah. Just, if you have time, take a look, let us know what you think, and if it makes sense to you.
Regarding the next steps, I really hope that we'll get this blog post finalized sometime next week.
We'll just publish it outside, and And yeah, that will be it. And then we will, of course, reach out to Victoria for sharing on socials.
Or maybe I will just do it myself, but it's always… there's, you know… always happy to reach out to Victoria for anything, so that was the plan.
But… View the doc.
Of course. Am I sharing my screen? I should be sharing my screen, I hope.
**Dhruv Ahuja** 20:13 Yes, yes, you're sharing Rusty.
**Andrej Kiripolsky** 20:14 Yeah, I see that Ashwini wrote that.
If you could view the dog.
**Ashwini Manoj** 20:19 Like, if I could go through it and…
**Andrej Kiripolsky** 20:22 Oh, yeah, of course. So we have AgendaDoc, let me share… Share link here… And a Zoom meeting, and I linked… To this document.
There.
Yeah, but it links to the research plan tab, so let me just relink correctly.
Okay.
Okay, so now it should be. Now it should be okay.
**Ashwini Manoj** 20:56 Yep.
Thanks.
**Andrej Kiripolsky** 20:58 Alrighty.
Sure. Dhruv, how… do you have any… anything that you didn't mention in your review, or anything you wanted to discuss about this?
**Dhruv Ahuja** 21:09 Yeah, I think the point about maintainers is valid, but I still think that excluding them makes more sense, because maintainers still have a way to just get together on a regular basis and just discuss things. So, I think there would be some sort of… You could say that drift between what the normal user encounters and what the maintainers do. Now, I know that when we did the data analysis, there wasn't as big of a difference in the final output.
But I still think that, based on the theme and our initial discussions, I would say that, I think excluding them is the right thing to do, but yeah, I would definitely love to hear what other folks have to say.
**Andrej Kiripolsky** 21:52 Definitely. This, like, it makes sense to me. I'm just, in general, quite anxious and undecided, so I sometimes just bump into this kind of, like.
Things like… both of them are, like, kinda correct, but I don't know for sure.
So there are pros and cons for both, like, including. So, we received a lot of responses from maintainers of OpenTelnetry and Prometheus.
And the question is whether we want to exclude them or not. So one thing that we did is that we excluded Vendor employees, because they have a stake in… in… hotel, they're selling their own hotel support, and vendor employees tend to skew the results towards, like, vendor products. So, for example, when we say that people run, like, custom custom collectors, or people… people instrument in some, like, very specific… vendor-specific way. And if we included vendor employees, we might… the results might look like That, like, in the community, people instrument or use, like, a lot of vendor stuff, but actually, it's really just a residue of having, like, a lot of vendor employees responding.
Yeah. So we excluded them, that's for sure. What we… And what we are discussing now is whether we should exclude also maintainers of OpenTelemetry, who are… who work in end-user companies.
Because they have, like, End-user perspective, but they… also can…
**Dhruv Ahuja** 23:28 Yes, please, Cole.
**Andrej Kiripolsky** 23:29 Yeah, they also can, like, share their perspective as a part of the hotel community, so… so the question is, like, if we want to keep them, and Yeah, or if we want to focus really only on end users who usually don't have a voice.
To… to… yeah.
To share their feedback.
**Dhruv Ahuja** 23:50 So, would, would maybe having a separate section, something like the, maintainer perspective, maybe… the title, just off the top of my head, where we come having the vendors, sorry, having the maintainers included versus excluding them like we have now, and what is the, like, what is the difference, or what is the, what is the trends queuing towards when we add them? Maybe we could report that separately.
**Andrej Kiripolsky** 24:21 Yes, yeah, good question. So, there are only 9 maintainers who are end-user, like, who work in end-user organizations.
So that's not really a whole, like, real big, big sample to have its own section about, but we can think about it.
And, regarding the… how data changes, it doesn't change, like, a lot. It… they add, like, 1%, like, up and down somewhere, but, like, the overall picture stays the same.
To me, it's more about… and that's why I want Arthur's feedback, is I want to understand… I actually don't know anyone. I don't know any maintainer from End-User organization.
And, I just want to make sure that we don't… like, that if we exclude someone, they don't feel like we forgot about them, or we disregarded their response, or something, something like that. Because I believe that for someone, it might be important. I believe that for vendor employees, this is pretty clear and straightforward, that's, like, the reason why we are excluding them. I don't think anyone would complain there, but if they are maintainers.
But End-Us at the same time, I think they might find it… be questionable.
But, yeah, let me discuss with Arthur, and I will definitely post the comment there. But, Dhruv, what you just mentioned, if you could also, like, just briefly write it to the comment, it would be… it would be…
**Dhruv Ahuja** 25:46 I'll do that.
**Andrej Kiripolsky** 25:47 Reported.
**Dhruv Ahuja** 25:47 I think… I think Ashwini's comment is also fair, that we could maybe just mention a note that the results actually did not change by including maintainers, so the picture overall remains the same, whether maintainers that are working for end-user companies are involved or not, that these are the patterns that are emerging.
So, I think I'll note down both of those things in the Google Doc today.
And, yeah, I just remembered I had, raised another question, let me go back to it. So, I had posted it in the, thread in the UX, Prometheus UX channel, There, there was a comment particularly saying that more examples using different language libraries, both trivial.
**Andrej Kiripolsky** 26:35 Oh, yes.
**Dhruv Ahuja** 26:36 That one. So, I believe we have missed including that.
So, do you think we should include that as well? Because I think it makes sense. What is our stance on maybe improving the docs, or what the current set of docs is?
Whether that work is already underway or not.
**Andrej Kiripolsky** 26:54 Actually, I'm not sure if I totally understand what you mean there.
So what kind of, what kind of examples,
**Dhruv Ahuja** 27:03 So, this was the, let me just, put this.
**Andrej Kiripolsky** 27:08 I saw your… I saw your comment, but I just… I don't understand what… what do you mean by examples for different languages.
**Dhruv Ahuja** 27:16 So this was the, this was the, feedback we had received over Tim.
**Andrej Kiripolsky** 27:21 Okay.
**Dhruv Ahuja** 27:22 was an end user requesting more, thorough examples, both the trivial ones and more complicated flows in different languages for Prometheus.
**Andrej Kiripolsky** 27:35 Okay, now I get it, now I get it. Yeah, this makes sense, this makes sense for sure. Let's, let's include that one.
Okay, let's.
**Dhruv Ahuja** 27:41 Let me just ping you in the thread again.
**Andrej Kiripolsky** 27:44 No, no, no, I have it opened, I have it opened.
**Dhruv Ahuja** 27:46 Okay, okay.
**Andrej Kiripolsky** 28:07 Cool, cool. So I will add that, I'll add that. That's a good point.
Alrighty, so let's, move to the next step, but as I mentioned, feel free to, like, anyone, feel free to… To add your… your feedback.
I have another good thing to mention, that Vidia Contributed guidelines for… Statistical significance reporting.
And, I reviewed, it's quite general, and It doesn't include, like, specific details of how to calculate statistical significance. At the same time, I think that these days with LLMs, we don't necessarily have to, like, provide formulas and stuff. This is something people can just figure out. And what I appreciate in VDS, Comment is that… Sorry.
that… It specifies how to how to… like, describe the… or, like, communicate the statistical significance in the blog post. So this is something that I will have to do also in this blog post, and I think it will be a good thing for the future to include that.
So, yeah, just wanted to give a shout-out to Vidya, and this is Merge, this is her first contribution, so… Super, super happy for that.
So, if Vidya will be watching from recording, thank you for that.
And, yeah, the next one, Dhruv, you have an update.
Yes.
**Dhruv Ahuja** 29:47 So, Dan is sponsoring my blog post. So, I had written it with a fellow engineer in my company, and I thought that it was a cool idea, and that we should actually try and get it published in the hotel website.
And I had raised the… I had shown the example, I… the blog itself, I believe, a couple meetings back. So Dan finally got the time to go and review it. I've raised the draft PR, and hopefully that should also be In the next coming weeks.
So, yes, thanks to Dan as well, if he's looking at the recording later.
**Andrej Kiripolsky** 30:27 I'll actually make sure that this is mentioned in the agenda.
Yeah, that's amazing, that's amazing. Super glad that folks picked it up.
as I told you, I would not be a good sponsor, because I just don't understand these things too much, but it's, like, Dan is, he used to work as SRE, as far as I remember, or on a platform team, so he has, like, very, very deep understanding, and he has been with the community for a longer time, much longer time than I have, so… And I think he, like, he will be a wonderful sponsor for this.
**Dhruv Ahuja** 31:03 Yes.
**Andrej Kiripolsky** 31:04 Cool! Cool, cool, cool. So yeah, good luck, folks, with that, and hope… hope we'll see the blog post soon.
Yes. And that's it from the… from the agenda. Does anyone else have anything, like, SIG End-User related that… like, project-related or work-related that they would like to talk to… talk about?
Or… Otherwise, we can… yeah, yeah. First of all, the first question.
Is there anything else?
**Victoria Nduka** 31:33 None for land.
**Andrej Kiripolsky** 31:35 No, no, no. Okay, no worries. Yeah, in that case, we ran out of agenda items, and I would be just curious, Ashwini.
you probably covered it briefly, like, the reason why you… why you joined the… these hotel meetings, and, like.
how would you like to… but yeah, maybe just… I would like to ask, like, follow-up there. So, have you thought about… contributing to something, and which area of hotel are you interested in contributing? Or do you just want to look around? We have people like that as well, right?
**Ashwini Manoj** 32:10 Okay, I actually found the blueprints interesting, because I was kind of building something like that.
like, within my, company. But when I saw blueprints was happening, I could relate to it, so… But I want to see what I can do. Like, right now, I don't have, like, an idea out of the box, but more, yeah, I, would like to focus on that.
**Andrej Kiripolsky** 32:41 Yeah, that sounds great, that sounds great. It's a part of, like, SIG End-User stuff, so… you might see some familiar faces there. They have meetings on Mondays.
It's evening.
So, it will be probably quite late for you, but it should not be, like, totally impossible. Like, as far as I remember, Oliver is in Australia, so for him, it would be, like, totally not doable, but I think for you it should be… It should be okay. Do you remember correctly, Oliver?
**Oliver Bassett** 33:11 You did. Well done.
**Andrej Kiripolsky** 33:14 Yeah, so, like, yeah, the time will not be great, but it should still be possible, if you are interested. And for sure, their meetings are recorded, and they are very… Ugh.
like, structured. They have issue templates, they have blog posts and stuff, so yeah, if this is interesting for you, for sure, take a look at that, and I think it will be an interesting thing to work on.
**Ashwini Manoj** 33:39 Yeah, sure, thanks, I'll take a look at that.
**Oliver Bassett** 33:42 That's 3AM for me. I was just looking at the calendar.
Not for me.
**Ashwini Manoj** 33:47 Yeah.
Yeah, sure. I'd say y'all. Wow.
Meanwhile, I'll also see what I can do here. Surveys look interesting as well.
So, yeah, let me see what… where else I can, you know, be part of.
**Andrej Kiripolsky** 34:10 Yeah, yeah. If you would like to do something here, in End-UserSIG, we have a… Issue board?
In GitHub?
Where you can check some… yeah, pick up work. Like, everyone is welcome to pick up, work that, that… We have in our to-dos.
There's stuff in progress that… We are trying to keep up to date. So, yeah, if you would like to do some of these things, or if you have any of your own ideas, totally feel free to propose them, and we are happy to support.
Like, in general, we would love to have more people from APEC region, Contributing.
with whatever they are interested in. So, yeah, we are definitely very supportive.
I'm dead.
**Ashwini Manoj** 35:05 Sure, we'll do that. Thanks.
**Andrej Kiripolsky** 35:09 Alrighty, and Maybe last quick question, Oliver, for you. You mentioned that you'll be looking around and trying to see something that is interesting and that you might want to contribute to. Were you, like, successful in the past couple of weeks? Like, have you bumped into something that is…
**Oliver Bassett** 35:29 No.
**Andrej Kiripolsky** 35:30 It was interesting.
**Oliver Bassett** 35:31 Been otherwise busy the last few weeks.
**Andrej Kiripolsky** 35:33 Oh, okay, congratulations.
**Oliver Bassett** 35:34 I've got a conference talk to prepare for in a couple of weeks, so once that's over, I should have some more cycles, so…
**Andrej Kiripolsky** 35:43 Nice, nice, nice. Where will you be, presenting?
Hiko.
**Oliver Bassett** 35:47 on Australia.
**Andrej Kiripolsky** 35:48 Okay.
Nice, nice, nice, nice.
**Oliver Bassett** 35:51 On a different CNCF project. Yeah.
**Andrej Kiripolsky** 35:54 That's amazing. That's amazing. Cool.
Alrighty, we're dead!
Dhruv, Victoria, if you don't have anything else, I guess we can just wrap up for today.
Nope.
Alrighty, so thank you everyone for joining, really appreciate it, and see you in two weeks.
**Dhruv Ahuja** 36:18 Bye, buddy.
**Oliver Bassett** 36:19 Thanks, everyone.
**Victoria Nduka** 36:20 Yes.
**Andrej Kiripolsky** 36:21 Bye-bye.
