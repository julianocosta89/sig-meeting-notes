SIG: CI/CD SemConv SIG
Date: 2025-07-03
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Johannes Koch** 00:49 Hello. Rotan!
**Dotan Horovits** 00:54 Hey, Johannas! How's it going.
**Johannes Koch** 00:56 Doing fine thanks. At least I want to say, Hi, I don't have much time today.
**Dotan Horovits** 01:00 Oh, okay, Gotcha, let me try and change the camera and the mic to something more decent.
Let's see if that works.
**Johannes Koch** 01:10 Are you back in in Israel.
**Dotan Horovits** 01:13 Yeah, back in Israel. Finally, let's see.
Oh, that's better.
I was really excited to see the message you sent me. Sorry for getting it with a delay because of all the travel and the mess that was happening around. But really I was really excited to see that you submitted that.
**Johannes Koch** 01:33 I don't know. I was like just trying. So you know, there is this. I don't know. The heroes have this track where we can submit stuff right? And it was 20 min before the deadline ended. Ron told me. Hey, Johannes, did you submit something for reinvent? And I said, Oh, no, I didn't. So I took the the 3 abstracts that I had finished right, and I just submitted them, and this was one of them, and without asking you. I just put you up as a second speaker right?
Because the Dev track claims to you should submit with 2 speakers or more.
I didn't know who else would be interested to talk about this, if not you right? So I kind of just decided on your behalf that if we get that talk, you would be my co-speaker without asking you. I hope that was okay.
**Dotan Horovits** 02:25 So 1st of all, thanks. I'm honored, obviously, to to join forces with you. And I did want to do something together, regardless. But so specifically just. I wrote you also on slack. I'm not yet finalized on on my invent, you know. You need some paperwork, approval and budget, and all of that. You know how it goes in in big, especially in Amazon, that.
**Johannes Koch** 02:50 I know.
**Dotan Horovits** 02:51 The Amazonians wants to be in reinvent, so they.
**Johannes Koch** 02:53 I know.
**Dotan Horovits** 02:54 Yeah.
**Johannes Koch** 02:55 I know, but having a talk always helps you to make your case right? So let's try if it works out. That's maybe good for you, and if it doesn't work out, then we at least try. That was my thought process when I submitted that thing so.
**Dotan Horovits** 03:09 No worries. I just want to, you know, don't want to mess things up for you if in case it does get selected. So I wanted to say it up front. And anyway, I think that if the talk gets selected, even if I can't go, I'm sure that we can find someone else from the 50,000 that come that go there. We just need to dig into the Sig and find who from the Sig is going to attend, and maybe even Adrian himself. So don't worry about that. Let's get it in, and then we'll exactly. That's what I thought as well. Let's see what happens, and exactly exactly but yeah, I'm I'm really excited. Like, if we get a slot to a bit of a stage time to talk about the Ci CD in general, and specifically the Sig. And also maybe tease some Amazonians and heroes and and other users to push for for support, because you've you've been fairly asking me a few times about what kind of support will be for the semantic conventions in different products, and I'm not on the product side of aws to comment officially on that. But But you know, hearing more more voices definitely at reinvent advocating, for that will definitely raise the awareness for the importance of adhering to auto specifications in in general, and the semantic conventions for safety in particular. So.
**Johannes Koch** 04:28 Yeah, we'll see. We'll see what happens. And at the end. And then at the end, it's like really just getting visibility into something is always good.
And and this is an initiative that I really much like right. And I think in aws, there's so much different forces forces driving product teams into different directions. Right? And that's yeah. Anyway.
we'll see cool for the sake I haven't done anything I really just wanted to say, Hi, usually I've been talking to Adr without anyone else on the call the last 3 weeks.
So we'll see.
**Dotan Horovits** 05:06 I should have done that before a few minutes before. But I'm out of shape now, with all the travel, and and I'll post here a reminder for everyone that this is taking place.
**Johannes Koch** 05:20 Yeah, so I will be. I will be away the next The next 4 weeks.
**Dotan Horovits** 05:27 Which is fair enough. It's summertime is, you know, vacation time for many. So not not surprising at all. It's it's fine. Any specific things that came up with Adriel on the last calls, just to know.
**Johannes Koch** 05:44 No, no, not really just a few reviews to do right. And then we talked a lot about the the requirement to come up with a little bit of a roadmap of what actually, the sick is gonna work on right? Because that's let's say you did that for the 1st quarter. I think right. And then you didn't really think about an update. That thing right?
**Dotan Horovits** 06:06 Yeah, yeah, no.
definitely and right right on time to have done here. He probably would second exactly this this ask to have. So it's definitely something. We started the discussing, raising, raising also with the obviously with the same con leadership. And the folks from Dan can speak to that. So saying, definitely, the need is there. We started the hashing through that. And I need to finalize and post it definitely. Hey, Dan, good to see you.
**Dan Gomez Blanco** 06:36 Good seeing you. Yeah. So on that on that front as well. We're trying to make that easier. That process of like starting a new project. So like we've got the let's say, phase one for ci CD, what comes now? Right? So I think, I think that's if we get this is something that from leadership, we're just trying to be better at which is defining like shorter scope, or like smaller scope for projects. And then we have a set of things that hey, we're gonna do this. We do it, we close it. And then we we move on to something else. Right? So yeah, I think that was if that's the if that's the idea, then yeah, very much welcome back. I'm happy to.
But you know, there's part of the initial project that was Cicd Syncov. There was a little bit of trying to find the the Gc. Liaison like myself, or the or the Tc. Sponsors and and all that that shouldn't need to happen again. Right? That's that's inherited from now that it's a sig. Now that it's a Cicd send com sig so if you want to define a new project, then it should. It should be fairly straightforward.
The only thing that needs to be done. There is, yeah. Open up here in the community. Repo is more of we're also trying to define like timelines, and you know, and deliverables in a way that I mean, it's open source. The timelines are what they are. But like. But yeah, just try to be a bit more clear to the community about that.
**Johannes Koch** 08:21 That makes sense.
**Dotan Horovits** 08:21 Good. Just a quick question about that. Then. So phase 2 of the Sig would be officially like a new project. Or how do you scope phase 2, or in general, like in other sigs.
**Dan Gomez Blanco** 08:33 Yeah, so it would be a new project. So the 6 still remains. We it wouldn't be So the same people.
Same, you know.
I guess whoever's in the Cicd synchron approvers Github team that will still be the same.
And it'd just be like a way of like. Okay, let's take that mark that project as complete the current one, and then try to set. Set up another one with another Projects board where you know, you can move things from one to another, right? So we just call it done for now and then. It's just a way to close the chapter right.
**Dotan Horovits** 09:10 Yeah, gotcha. Okay? So essentially, we once we scope it, we open a new project with a new board. And you know, of course, we can move some tasks that we decided that fell off the phase one and moved into phase 2, just, you know, reinstantiate them in the new board right.
**Dan Gomez Blanco** 09:29 Yeah, as a, as a, as a golden golden child of a reporting on things. So yeah, it's it's been very clear so far. And I think that you know, taking those deliverables and into another one. That would be that would be awesome.
**Dotan Horovits** 09:44 Yeah, yeah, that sounds good. And yeah, we have new joiners. Relatively. Johannes has been on the call. So for quite some time. He actually just updated me that he's going to maybe look for a stage to talk about that and help us spread the word out. So really exciting to also have more advocates out there.
Maybe also on that opportunity I can share with you that I just came back from Open Source Summit in North America, in Denver, the Linux Foundations Conference, and I had.
I used that opportunity as well to share about the Sig. And actually in a perfect setup like, because they have the Cdcon sub like event or like. So it's really good, because this is with the CD foundation folks and good audience for this for this. So.
**Dan Gomez Blanco** 10:34 Nicely.
**Dotan Horovits** 10:34 Yep.
So I think we're not. We're not going to have too many folks today on the on the line. I didn't see anyone responding also, not Adriel. So I guess. Let's see what we want to cover today in terms of I won't do the I won't run the triage, because, unfortunately, I'm out of date, just coming, having back, coming back from travel. I I myself need to think so unless someone of you wants to.
take it. Take the lead on this one. I guess we can just see if there are any specific topics that you want to cover on the agenda today.
**Dan Gomez Blanco** 11:11 Yeah. Got a question?
**Johannes Koch** 11:12 Do that.
**Dan Gomez Blanco** 11:13 Tool, but I'll add it to the agenda.
**Dotan Horovits** 11:17 Yeah, actually, let me just make sure that I open it, you know. Can you throw the link here on the chat? And then we have it also on the call, and everything recording and everything.
**Dan Gomez Blanco** 11:28 Trying to find it. There we go.
there we go.
**Dotan Horovits** 11:33 Perfect.
**Dan Gomez Blanco** 11:36 June 26, th was the last one.
**Dotan Horovits** 11:37 Yep.
**Dan Gomez Blanco** 11:38 It's great!
**Dotan Horovits** 11:38 This.
That's only July 3.rd But other than that.
**Dan Gomez Blanco** 12:08 And yeah, just put your name in there. If you want.
**Dotan Horovits** 12:22 Johannes feel free to get yourself also listed. And yeah, Dan, you wanted to add some agenda items there.
Oh, then the new time, I see. Now. Okay.
**Dan Gomez Blanco** 12:32 Yeah.
**Johannes Koch** 12:38 I think the poll didn't return any meaningful results is what Adriel said last week.
**Dan Gomez Blanco** 12:49 Right. Oh, there, there he is!
**Johannes Koch** 12:51 I mentioned him too often.
**Dotan Horovits** 12:54 Even 2 of them. Hey, Drew. Good morning.
**Dan Gomez Blanco** 12:58 Say his name 3 times.
**Adriel Perkins** 13:00 And good day, though.
That's hilarious.
**Dotan Horovits** 13:03 You're covering for your absence by having double. Huh?
Yes, hey? Drew? No.
The way to go.
**Adriel Perkins** 13:11 What's in the matrix.
**Dan Gomez Blanco** 13:13 Hmm.
**Dotan Horovits** 13:14 All good, all good thanks for for joining. It's early time your day, but just goes to say about the new time survey.
**Dan Gomez Blanco** 13:24 Yeah.
**Adriel Perkins** 13:25 Yeah, it looks like it's gonna be. I think it's gonna be 9 the same time this tomorrow or the day before.
**Dan Gomez Blanco** 13:32 Wednesday.
**Adriel Perkins** 13:32 On yeah. Wednesday.
**Dan Gomez Blanco** 13:35 So we got is that we got 8 people in that one.
**Adriel Perkins** 13:39 Yeah. And I talked with Christoph. He won't. He won't be able to make it right now, but as soon within 4 months he'll be able to make that time, though he works out.
**Dotan Horovits** 13:55 Oh, wow!
Wednesday is a bit of a tough day for me personally.
just because too many calls with the Us. Fall on that.
**Dan Gomez Blanco** 14:08 That specific day.
**Dotan Horovits** 14:11 But we'll go with what the community prefers.
**Dan Gomez Blanco** 14:19 Wednesday is, I think Wednesday is normally my, my hotel day quite like quite a few, but nice but cool.
yeah, I mean. That was the only thing that I I wanted to ask.
I've been trying to, you know. Speak to other folks that are not on the vendor side, but on the end user side of things to join.
I don't think they voted in that, but I will share it again with them.
**Dotan Horovits** 14:55 And I see important names like Velin. I think her that would be good to have, like the folks from Team City to see how this progresses. And obviously we mentioned Christoph once he's available. Let's see that the folks that are that are really relevant. I can can make it. I should say that kale is unable to do Wednesdays.
Hmm!
Bit of a shame whe! When do we do want to do the the cutoff.
What are your thoughts on converging on this one.
**Johannes Koch** 15:47 My advice would be, wait for the summer break to go over, and then start fresh.
**Dan Gomez Blanco** 15:54 That sounds like a good idea.
**Johannes Koch** 15:56 So that would be something like, I don't know mid August.
something like that, right? And then I think that's something that you that you also that we also could then somehow plan right in terms of.
**Dan Gomez Blanco** 16:07 Yeah.
**Johannes Koch** 16:08 Coming up with some marketing like joint approach of. We're going to relaunch this with a new date, and everyone please attend and then do some kind of I don't know. We can give away some gimmick, swec. Whatever credits, whatever.
**Dotan Horovits** 16:25 And we can piggyback on, you know, starting the new project as I, just, we just talk about like phase 2. So okay, for phase 2. We're looking to refresh. We'll have the new project. We'll have the new times, if needed to adapt. Of course, maybe can also use that as like a compelling event for folks to converge. By the way, I'm just looking to see Alan is not here either. Right?
I'm just looking to see folks that we know that have been involved, and regulars to make sure that they can attend. Have you heard from him, Adriel, by any chance?
Not sure we have, Adria. I think he's.
**Adriel Perkins** 17:14 I have. I have not heard from Alan in a while. I mean.
I don't remember how I did the poll. I think I copied the poll forward from the original poll, which is why it had that whole 2024 date I was hoping that people might select like times that are, we're not on there as well. Just to get an idea of like what times work, what other times might be available.
Yeah, if we're gonna wait till August.
What are your thoughts around adding more times to the poll and getting people to selected it again just to get, does that make sense. The question makes sense.
**Dotan Horovits** 18:02 No, if we're, you know, relaunching it in August. The poll, we can obviously do that with different options.
My experience with polls is when you have too many options, people get confused. So just need to make sure that we.
And still we can obviously offer the other and have get people to comment, at least with, with what else could work for you? But that's fine, like I happy to add more more options.
I can say on my end personally, and maybe for others in in Europe that work with the States. I think the early time, like later times of the day, tend to conflate with the Us.
Spent time. So for me it was convenient. It was like, it's 4 pm. My time. It's 3 Pm. Central Europe time.
I think, in that regard, Dan. Probably you can comment on that experience from your end as well, but like it, it was convenient in terms of like. Then you you're not conflicting with the the main bulk, whether Cncf. And foundation for front or or work front. But yeah, I know it's early on the other side for for you, Adriel, and if we get some fall for mountain time or or pacific time, it will be very harsh. So yeah, sorry, Daniel, you wanted to say.
**Dan Gomez Blanco** 19:22 No, no, I agree. Jason, yeah.
**Dotan Horovits** 19:30 Anyway, let's say it's a good decision to just revamp it after the summer break, because many now are unavailable, anyway. Johan has just said that like 4 weeks now, he won't be able to attend the calls obvious for obvious reasons, and then others. So maybe looking fresh and taking it again another round, maybe with some other or additional options.
Beyond that, Adrian, we talked before, just before you joined about sort of the the process of like closing the project, opening a new one. Daniel also shared about some work to simplify the procedure so.
and just wanted to to loop you in on that one as well, so essentially, phase 2. To to be instantiated as a as a new project. After wrapping up this one.
**Adriel Perkins** 20:32 Yep, sounds good. That's I'm looking forward to that. I need to do some cleanup of the general issues and things. And I'd like to actually, before we instantiate phase 2 have the work a little bit more clearly defined and easy to pick up for that phase.
**Dan Gomez Blanco** 20:53 That will be.
Yeah. I mean, that would be awesome when we do the the project proposal that there's a little bit at the end where we say.
**Adriel Perkins** 21:01 And.
**Dan Gomez Blanco** 21:03 If you have a Github project like a board, right?
**Adriel Perkins** 21:07 Yes.
**Dan Gomez Blanco** 21:08 You don't need to create it initially, but if you have it.
that's great, because that already has the things in the, you know.
like, what is the initial? What is the initial things? Are you going to be working on in that? That would be awesome. Yeah.
**Dotan Horovits** 21:21 And that also serves what we talked before about like transferring the ones that we that fell out of scope for phase one. And we still want to keep, because it's also an opportunity for cleanup for things that we don't want at all. We see a realization. But the ones that just, you know, want to move over. It's it's, I guess, an easy transfer migration phase.
**Adriel Perkins** 21:41 Exactly, exactly.
**Dotan Horovits** 21:43 Yeah, Adrian, and let's follow up like happy to to work with you and see how I can help. And let's what's the easiest way to to go through that and obviously with Dan's guidance, and to do that.
**Adriel Perkins** 21:59 Sounds good, appreciate it.
**Dotan Horovits** 22:02 Beyond that, Adrian, do you want to run the trials, to to take control on and lead that part.
**Adriel Perkins** 22:12 I'm on Mobile right now.
but I can talk to what is on the board.
**Dotan Horovits** 22:20 Okay, so let me just, or you know what, Dan, do you want to share that on your side, or.
**Dan Gomez Blanco** 22:27 Yeah, can do a second. I need to go back to got a switch tap. And now ignore this.
**Dotan Horovits** 22:37 Too too many tabs.
**Dan Gomez Blanco** 22:41 One second like got it, and that's the one so triage on this project board.
or do we want to do any other?
Or is that.
**Adriel Perkins** 23:19 Yeah, it's that that one's it.
Again, that top one. I'll just give a little update about it.
waiting for one more round of feedback to get through.
You got it 3 approvals from Carlos, Robert and Riley. I think there were just a couple of more nits for things that I need to maybe go through.
**Dan Gomez Blanco** 23:52 Okay. Cool.
**Adriel Perkins** 23:54 Yeah, so that should be good. That's it. It turned into supplementary guidelines instead of propagate envy and are propagated.
But there are 2 prototypes that are drafts that are open. One go one in python. I open the one in python, Robert. Open the one and go so as soon as this is merged, hoping to take a stab at actually getting those prototypes and the hotel libraries, and start getting that support to the languages, which would be.
I think that's even better than having the stack, because then it's having something that actually works.
**Dan Gomez Blanco** 24:36 Yeah.
makes sense.
**Adriel Perkins** 24:43 Feel free to take a look, though, and ask questions.
**Dan Gomez Blanco** 24:50 Okay, okay, so that's yeah, that's still basically work in progress. I guess that yeah, review comments right?
**Adriel Perkins** 25:00 Yep, the gatelab pipelines one it's had 2 iterations thus far.
Nicholas is planning on working on the next iteration in a few weeks.
So it's just taken its normal large period of time with contributing to the hotel collector for the 1st time.
**Dan Gomez Blanco** 25:21 Kind of thing.
**Adriel Perkins** 25:23 That's but people are asking for. I don't know if you all saw that get loud. Decided not to pursue anytime soon pipeline placing so
**Dotan Horovits** 25:39 Yeah. Super.
**Adriel Perkins** 25:40 More impactful.
**Dotan Horovits** 25:41 Super disappointing.
They don't want, like native 1st citizen support of this thing.
**Adriel Perkins** 25:53 Yep.
And it's not like it's actually that hard to implement.
Anyway, it's a it's a cost thing, I think, or a I don't know. Everything's being shattered by overshadowed by AI right now. So maybe in a few years, though, pick that stuff back up.
**Dan Gomez Blanco** 26:12 Yeah, it's like, Oh, we don't have time for this. We need to implement more. AI, yeah.
How do you observe that? AI. I don't know. We'll think about that later.
Okay, in this one.
**Adriel Perkins** 26:30 This is one of the things where like this has been open for so long that in phase 2, I'd like to take these things into bite size chunks, so they can actually just go progress instead of being open for 7 months.
**Dan Gomez Blanco** 26:44 All right this would be for, like self-hosted runners and things like that, right?
Is that.
**Adriel Perkins** 26:49 Oh, sorry for that. Let's see.
**Dan Gomez Blanco** 26:52 Define conventions for associated host, port metrics.
**Adriel Perkins** 26:56 Yes, yeah, that's good.
And I believe Kristoff has a Pdr. Open 1, 2 that I probably still have yet to review.
And then that should close anyone's welcome to review things.
So even if you you don't have like, even if your approval doesn't count as an approval, quote unquote.
we certainly appreciate the feedback in the room, anyway, because that that does really help us. Let let us know that, like people like me are looking and like they're interested or like, they think this might be a good idea, but is is anyone's welcome to approve.
**Dan Gomez Blanco** 27:41 Cool. That's the Pr right here. So I think, yeah, this last one.
That's the one.
**Adriel Perkins** 27:47 Yes.
**Dan Gomez Blanco** 27:55 And Kim City.
**Adriel Perkins** 27:58 I've not heard since this since we had that meeting on this one.
which also means for phase 2. If I still haven't heard like.
Maybe it's best to just close it as like unknown, not done or not known. If it's done, and just move on and let it come back up once it importance.
**Dotan Horovits** 28:27 Make sense.
Do you know who currently is the owner? Is that still.
**Adriel Perkins** 28:34 Well, you can't be the owner. If you're not like in the list of approvers and things within hotel so like it took me forever to get Christoph to be able to have the ability to be assigned to him because he has to be an approver and like the Maintainership stuff
**Dotan Horovits** 28:52 No sorry, I mean I should have phrased it better not the owner in in terms of the Github Repo, rather than who's the who leads this from from this initiative? Obviously, you're updating on their behalf. But is that still?
Or because she mentioned someone else from the from the company? Another lady that she said that like she will be more focused and like there were discussions on on other names. But I'm not sure who ultimately came up.
**Adriel Perkins** 29:19 Got it. Yeah, no, do. I do not know. I do not know. My understanding was that between them they would handle updating this and and let us know on status statuses. But I just haven't heard from.
**Dotan Horovits** 29:35 You got you?
Because there was also the the I forgot his name, the gentleman from Australia? Or was that that separately, like he had this integration, that, and then, when when we got them together there at Kubecon, it looked like a good place for collaboration. But I'm saying if if the team city team cannot move it. Maybe the the other initiative, just wondering if you heard anything on on that other angle.
**Adriel Perkins** 30:04 I have not, unfortunately.
**Dotan Horovits** 30:06 Okay.
no worries. Just let's let's keep in mind that there was like another path. Obviously the the native one by the vendor is always the the preferred one.
But if it reaches that end, at least we had, like another lead, potentially for for the team city integration.
I need to dig up the names. I'm sorry I like. I blank out on the on the names. But Adrian, you probably remember what I'm talking about right.
**Adriel Perkins** 30:32 Yeah, I don't remember his name, but I I do remember his face.
**Dotan Horovits** 30:37 Yeah, yeah, okay.
**Adriel Perkins** 30:44 And the to do side.
Those are still, I think, yeah, I mean, they're still. They're just where they're at.
I'd love to get them done. I haven't had time. No one's picked them up.
Understandable.
**Dotan Horovits** 31:01 No, no, fair fair enough lots of things that you're taking care of, and and thanks so much for for leading that.
I have a related question about talking about Team City. Do do we have anything about Jenkins? Again there was the initial discussion and interest. But not really, I think it's Cyril. If if I'm mistaken from Grafana labs right.
**Adriel Perkins** 31:29 Haven't heard from them since the original conversation we had.
**Dotan Horovits** 31:35 Okay.
Okay.
So let me write down, for, like, I'll try and ping them again and follow up and see if there's still interest.
So one second I'll just write quickly.
I know it's part of the trial, but I'll put it as a separate bullet for integrations.
Is Evelyn still driving this.
And Jenkins, we have.
Okay.
Sounds good.
I think we covered like, is there anything else that you wanted to cover on the trials? Adrian.
**Adriel Perkins** 32:37 Yeah, that's it.
**Dotan Horovits** 32:38 Okay, sounds good. So I think we're we're good on this one as well.
Let me know. Does anyone else have any other agenda items for for the meeting.
No, okay. So give you the the time back. And yeah, then let's follow up to see how to run the formalities with the with the new project following your lead on this one.
yeah. And adriel, just a note. I got to brag with your achievements there on last week and Open Source Summit showed them how you used cicd obsobility to help hotel.
The good old story resonated very nicely with the folks at the open source summit and the Cdcon. So.
**Dan Gomez Blanco** 33:30 Nice.
**Dotan Horovits** 33:31 If you're getting any pings from folks from the community, it's my fault.
**Adriel Perkins** 33:37 Thanks. I appreciate it. Glad glad you were able to go, and glad you had a good time.
**Dotan Horovits** 33:43 Yeah, it was a good good opportunity to meet folks by the way, they they did ask a question that, to be honest, I know that we've been discussing it from day 0 from the original scope, but I feel that I don't have it brushed yet. The the resolution of this back and forth with the team about the city events.
How would you? I'm curious, both of you, actually. How how would you phrase this? I know we're discussing them within, and it didn't end up seeing like there is like each one has its own. But how would you more clearly articulate this the the gap, the decision, the the different scopes.
**Dan Gomez Blanco** 34:27 On the sorry, which one, though.
**Dotan Horovits** 34:29 See the events.
**Dan Gomez Blanco** 34:32 Or CD. Events.
**Dotan Horovits** 34:33 Yeah.
**Dan Gomez Blanco** 34:34 And but I guess you know, like the scope of I guess someone was trying to sort of like extend the scope to incident management as well. Was that like the the?
So I do think there's a difference here between like events coming from, I guess deployment pipelines, to which I think you know.
would definitely be to me. That would be under the scope of their sake, right in the future.
But there's the other aspect of like the change failure like the instant. I think the instant I think that's that's the 3.rd That's almost like, you know, you keep expanding the scope right. So I think you know not that you know. Not that I don't think could be covered in the future, but I think how I would explain it probably would be that it's open sources.
and especially open telemetry has the the challenge of trying to do trying to go too wide.
So we have limited bandwidth.
and we need to, I guess.
You know. Trust on the Sig leads like yourselves to to decide what is the the current thing to focus on and then try to get the community at the end of the day. It's open source. You can't really tell people what they should be doing right, or what they should be working on. Everyone is doing it sometimes on their own free time. So and if someone wants to work on something, it's always welcome.
But we should encourage people to focus on the things that are the most priority, or that we have decided is the most priority. And then, you know, after that is done, we can focus on other things right.
**Dotan Horovits** 36:19 So yeah, it's my you view. See, the event is like more on the on the incident management. Right? That's like the the.
**Adriel Perkins** 36:27 It's got a lot it. It does have Cicd so I guess. Let me let me take a step back a little bit. We do have incident stuff related stuff on our board.
You know that in part of the reason why I put it there is because the the information that we are semantically making is information you need for Dora. Dora's purpose is to measure the effectiveness of your Ci. CD, that does include incident.
**Dan Gomez Blanco** 37:02 Yep.
**Adriel Perkins** 37:02 You. You require incidents to be able to calculate that information. So that's why it's a little bit of backstory. Why, I put that there.
I think we still do need it. But we certainly haven't been something. A priority. See? Events, on the other hand, though, is is basically events from your build system, just general log event structures that have like predicates and various different nuance to them. The original proposal for our semantic conventions the 1st pass was to use CD. Events, CD. Events is still viewed as experimental inside of the open cemetery semantic conventions. It is valid.
It is shown as experimental. Alongside is part of cloud events kind of like inherited by the cloud events back. So we we support cloud events, cloud events supports 80 events.
therefore we support both as experimental, or allow both. I should say I don't know. We support the foot.
The original proposal actually had allowed outlined it to be very similar to CID CD, and in fact, I think it was literally like we should use CD events and the community and the powers that be really disagreed with that proposal. They wanted to be more agnostic across the board and build the attribute schema according to the open telemetry attribute file, make it more agnostic, and and make it more annotable to all sorts of telemetry. Not just like you have to pass them an event right? Which is one specific signal.
So from that perspective we went with making again it more agnostic any of the verbiage, making it attributes, and so forth.
and CD events.
We haven't really talked with them since, and there is a lot of overlap like I get questions all the time at work. I want to be careful saying this because this is a recorded call, but, like often what I hear people say after they understand the Hotel semantics is that? Oh, so there's really no need for CD events.
And you know, on one hand, unlike.
yeah. Basically. On the other hand, I'm like, it's also a Cdf project, right? Like, I don't want to shoot anyone's project down. And I think there's still value in that but yeah, I mean, if you annotate all your stuff with.
it's open telemetry, semantics. And you really don't of a huge need for any type of CD event thing. Maybe there's some specific systems that already emit those events. In which case, like tucked on. In which case it's like, Oh, yeah. Well, it's already there.
Use it.
But I would love, I mean honestly like like.
if I had like a dream, it'd be great to just say, Hey, like, let's just merge CD events into hotel. Call it all one thing. Get the manpower, and that project goes away, and merging part of hotel, and away you go.
That is not something that I'm capable of doing. I don't know how I begin doing that other than my talking to people. But yeah, right now they're just 2 divergent projects that are highly related.
and the hotel can provide CD events. But we have not done anything like concrete with really supporting it or incorporating it beyond that original proposal which really got denied by the community.
**Dotan Horovits** 40:52 No, I think you you run into this question. I run into this question as well. I'm sure Dan probably encountered that at least once or twice so, and I'm saying, obviously this is a under the sister foundation. Cdf, I don't want to. On the one hand, I don't want us to be perceived as because it's a different foundation, like we're going about our own ways without disregarding them, and I keep on emphasizing that even the original scope of the Sig, or even the Otep that preceded it, already flagged the CD events. And we've definitely been engaged them in these early phases.
I just I guess I would like to. Just think of what would be our internal understanding. That's A and B. What would be the best way to communicate.
not not to the Cdf. The CD. Events folks, but to broader audience. To make sure that we keep the door open. We relay the, you know, definitely happy to collaborate on looking at merge, or any something that will make sense to align.
I guess that's why I'm asking, because you you both have very, very good perspective on that probably better than mine to to comment on that.
anyway. Thanks, Adriel for the perspective. And I definitely I don't want to disparage any. Anyway, any other project or foundation. So this is why, and especially when I go to this audience, I want to make sure that the message comes through as.
on the one hand, there are some specialty areas where each one took a different path or a different, I guess, focus area. On the other hand, there is an overlap and room for discussing when the time is right, and when the teams are ready for that, or something like that, to make sure that the the place is there to to discuss.
**Dan Gomez Blanco** 42:59 Cool.
**Dotan Horovits** 43:00 Anyway. So that's that's just I wanted to share from last week's open source summit. And and yeah.
I'll I'll I'll give you back the time, unless there's any anything else.
**Dan Gomez Blanco** 43:14 Not from my side.
**Dotan Horovits** 43:15 Cool thanks. Everyone have a good one.
**Dan Gomez Blanco** 43:18 Cheers. Bye-bye.
**Adriel Perkins** 43:19 See ya.
