SIG: Governance Committee
Date: 2026-02-18
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/4Xi2O1kcgF2p5uezfT-zOxwCmrKEmDcGJSmUG-yqVr80k0fpigfFYGZHz1UGz_oo.EnOmdYtK4NH3cl60
============================================================

## Zoom Recording Transcript

Austin Parker 00:00:21 Howdy.
Marylia Gutierrez 00:00:23 Boom.
Trask Stalnaker 00:00:40 Hello!
Austin Parker 00:00:42 Woody?
Pablo Baeyens 00:01:06 Pete.
Trask Stalnaker 00:01:25 Maria, are the meeting notes… problem that the profiling SIG is having.
I don't know of a… any other option, so, I mean, I think it's…
Up to them if they want to lock it down to a specific named people…
I guess, can they manage… the question is, can they manage those permissions themselves once you add them, so they don't always have to go through.
Marylia Gutierrez 00:01:58 Yeah, because I have to, like, keep adding people to the group. So that's why I was, like, searching if there's anything, just, like.
Only people dedicated, but no, all the options are always like, yeah, you can give to a specific group and have to update that group.
Trask Stalnaker 00:02:14 So I think you can… oh, go ahead, Pablo.
Pablo Baeyens 00:02:19 I was gonna say maybe the group…
doesn't need to be owned by the OpenTelemetry org, necessarily. I don't know if that's a good idea, but if we want to give them
that power.
Trask Stalnaker 00:02:33 So, I think we can do this. So here's their Google Doc.
Oh, I have to…
Is it?
Owned by admin, or owned… it's probably owned by…
Pablo Baeyens 00:03:02 I think those are owned by… governance committee. Yeah.
The auditor.
Trask Stalnaker 00:03:44 What, since I'm struggling for… off here…
What I'm remembering is that on the sharing page, there's a setting to allow people with edit permissions to change the permissions.
And we uncheck that, because we have global edit.
But if you check that, then they might be able to, once you give somebody bootstrap it.
With someone with edit permission, you might be able to
They might be able to manage permissions.
Marylia Gutierrez 00:04:58 Who is the liaison for the profiling one?
Morgan McLean 00:05:02 That's me.
Marylia Gutierrez 00:05:04 Okay.
Maybe we can take this into action, so we don't spend a lot of time on this meeting just trying to log in to stuff.
Trask Stalnaker 00:05:24 Sounds good.
Allow editors to change permissions and share, yeah. So it looks like it should be possible, but
So this is the, kind of, the hidden setting here.
When you go to sharing…
Up here, the settings, it's this one. We uncheck it.
But if you lock it down, then you could check this, and then I…
Thing, then they can add more people on their own.
Marylia Gutierrez 00:06:39 Wanna go to the first item, then?
Trask Stalnaker 00:06:43 Cool.
Ted Young 00:06:49 Dude… Well, first thing is just Severin saying.
check out this update to the GC Charter, which is, like, a pretty vanilla update, but everyone, please go take a look at that.
Alolita Sharma 00:07:04 Okay.
Trask Stalnaker 00:07:04 Yeah, looks like we have 4 GC approvals.
So maybe if we include his, that's majority.
So we could merge.
Ted Young 00:07:16 Yeah, I can approve it as well. I don't… I think it's, like, a pretty milquetoast change, so I don't…
Morgan McLean 00:07:22 I'm just going through it right now.
Alolita Sharma 00:07:24 Yeah, I'm going through it, too.
Let me just switch over to it.
Trask Stalnaker 00:07:53 For the next one, the Zig Zig…
It looks like we have, feels like we've got enough… people on board?
For that to be a reality.
Including, Jacob, Aranov,
Has volunteered to be at least a bootstrap maintainer for it.
And they have… Also, Kamal, who's…
been part of the compile instrument… Go Compile Time Instrumentation SIG.
And then they've got a… 3 or 4 new people.
Who volunteered.
Austin Parker 00:08:45 Yeah.
Trask Stalnaker 00:08:46 So, I… I think it's good to… Go forward…
Austin Parker 00:08:53 Yeah, so I see 4 people plus… Jacob. Jacob.
Trask Stalnaker 00:09:01 Oh, and oh yes, the four people included in, francesco.
Austin Parker 00:09:10 Yeah, Giovanni…
Trask Stalnaker 00:09:19 And good distribution of content.
Austin Parker 00:09:21 Yeah. Yeah, yeah. No, I think that's good.
Ted Young 00:09:26 In terms of, like, GC liaison and TC Sponsor, it seems like those are things that have to get picked, but…
Austin Parker 00:09:35 Yeah, but I think… didn't Jarber…
Trask Stalnaker 00:09:41 Josh seemed semi-interested.
Austin Parker 00:09:43 Jacob, or not Jacob, bud.
Trask Stalnaker 00:09:47 Josh. Josh, Josh McDonald.
Austin Parker 00:09:49 Also seemed interested, right?
Trask Stalnaker 00:09:53 Josh Saret?
Maybe…
Austin Parker 00:09:56 I thought both Josh was…
Trask Stalnaker 00:09:57 Both patches, okay.
Austin Parker 00:09:59 That's what my… my recollection is both Josh's.
Alolita Sharma 00:10:03 I definitely think Josh McDonald was interested. Yeah. I mean, he had…
Ted Young 00:10:09 Osterith is over… perpetually.
Alolita Sharma 00:10:11 Over the nose.
Austin Parker 00:10:13 Oversubscribed.
Ted Young 00:10:14 I would recommend the McDonald's.
Yes.
Austin Parker 00:10:17 Really?
Yeah, I mean, I also…
don't necessarily… I think if… especially if Jacob's involved, I don't necessarily feel like it needs…
the highest level of TC involvement?
Trask Stalnaker 00:10:32 Yeah, that… that was my…
goal for reaching out to Jacob was, that, yeah, then TC would feel comfortable with, like, their minimum
involvement.
Austin Parker 00:10:45 Yeah.
Trask Stalnaker 00:10:46 I can ask, as far as GC liaison, does anybody… Want.
the project?
Alolita Sharma 00:10:57 Trask, I can support it, because I only have, two. I think, Pablo took this Prometheus group, so…
Trask Stalnaker 00:11:06 Okay.
Alolita Sharma 00:11:07 Yeah.
It just depends on when their meetings are, so I'll coordinate with them. I can… and I can, so we are selecting Jacob? We are okay with Jacob?
When the trees to answer?
Trask Stalnaker 00:11:23 No, not a… I mean, he can't be TC Sponsored.
Alolita Sharma 00:11:25 Right? Because he…
Austin Parker 00:11:26 Right, but…
Alolita Sharma 00:11:27 But again, I'm just sort of…
Austin Parker 00:11:29 But if he's involved, then I think we can say, hey, the TC doesn't have to have, like.
Alolita Sharma 00:11:34 Full-time support.
Austin Parker 00:11:35 Josh Shareth level of, like, day-to-day involvement, and maybe, like, JMACD could.
Ted Young 00:11:42 Whatever the lowest… Yeah, that'.
Alolita Sharma 00:11:44 That's fair.
Austin Parker 00:11:44 Yeah, we just have to talk to… we just have to talk to them.
Ted Young 00:11:46 Like, the point of contact level of sponsorship.
Alolita Sharma 00:11:49 Yeah, yeah, I can definitely…
Ted Young 00:11:52 Support that.
Someone will have to do a review of their stuff from the TC, but it doesn't have to be this person.
Alolita Sharma 00:11:58 Okay, sounds good.
Trask Stalnaker 00:12:00 Cool, since I've been chatting with them, I'll take the follow-up of, I'll check with
Josh McDonald, and then I'll…
summarize on the… the issue, Alolita, of where we're at, and then I'll ping you and kind of hand that off to you.
Alolita Sharma 00:12:17 Okay, okay, Trask, sounds good. Thank you.
Trask Stalnaker 00:12:25 Severin's gonna be so happy.
To have the.
Alolita Sharma 00:12:29 And they moved. Zig, zigz.
Austin Parker 00:12:31 Say that five times fast.
Alolita Sharma 00:12:36 I… It'll be the new question to ask our new…
Austin Parker 00:12:40 Members.
Ted Young 00:12:43 Well, speaking of Severin, he's.
Marylia Gutierrez 00:12:46 Actually, just one tiny thing, just to keep up, I was gonna say, speaking of, like, music, Alolit, I think the Kotlin is still waiting for the Zoom.
Alolita Sharma 00:12:54 Yes, they are. I finally got all the permissions, Marilla, so I was working in the background, and their meeting is next week, so…
Definitely.
That'll get them set up. They're waiting for a calendar event and the dock.
Ted Young 00:13:14 So, Severin's got a blog post coming out about KGATE.
Austin Parker 00:13:19 Cas… I know, Casper does… I don't… Cool, draft maturity model…
I don't quite understand what this is… Asking…
Is it okay if we make a blog post that references this draft proposal? Is that what this is asking?
Ted Young 00:13:51 Which one are you looking at?
Austin Parker 00:13:55 the… KGateway blog?
Trask Stalnaker 00:14:00 It references this… maturity model, proposal, in the community.
Juraci Paixão Kröhling 00:14:08 I think… I think this is the wrong blog post.
Let me take a look, because I think Kaspar has another blog post about the maturity model.
Ted Young 00:14:19 Yeah, there's a second link.
Austin Parker 00:14:22 I'm… yeah, so I'm looking at the maturity model…
Pablo Baeyens 00:14:37 Want to link the… is on the meeting notes. There is a reference to the maturity model.
Austin Parker 00:14:44 Right, I just haven't seen this maturity model until now.
I…
Alolita Sharma 00:14:57 Isn't it a bit complex?
Trask Stalnaker 00:14:59 The blog post, so it says, will evaluate behavior using a draft maturity model.
Austin Parker 00:15:09 It's a… Pointing to the community issue.
Pablo Baeyens 00:15:16 Right, it doesn't allow early… Stop listening.
Trask Stalnaker 00:15:23 Sorry, what was that, Pablo?
Pablo Baeyens 00:15:26 I think the blog post, at least the one that, Severin Link, does not say that the maturity model is an established thing, it just mentions that.
This thing exists on a community issue.
Ted Young 00:15:42 It feels a little transient to be referencing in a blog post, but again.
Alolita Sharma 00:15:46 Yeah.
Ted Young 00:15:47 Zoom.
Alolita Sharma 00:15:48 No, no, but, I mean, again, a lot of end users read this, so is this something that we are ratifying?
From the project?
Austin Parker 00:15:57 That's my concern, yeah, just, like, from looking over this, I…
My short concern is that there's a lot of stuff in this
And just for… so we're all on the same page…
I'm gonna put the actual model that Casper wrote in… the actual model that's… like, this is what is actually being talked about when they talk about this, like, support maturity… totally support maturity model.
Ted Young 00:16:28 So this is a little… maybe a little too much.
Austin Parker 00:16:31 This seems a bit much, especially because it's talking about things that, like…
Alolita Sharma 00:16:38 Wow, that's really a lot.
Ted Young 00:16:41 I mean, this is all cool, I'm happy for people to try to, like, get stuff organized and help out, but maybe we should talk to this person and…
Austin Parker 00:16:50 Yeah, like, I'm…
Ted Young 00:16:51 Game plan.
Austin Parker 00:16:52 Well, I think… yeah, I think my big thing is just, like…
I don't know, I just see stuff in here that feels like…
I don't know if it's, like, aligned with the vision…
I think there's stuff in here about, like… like, there's this whole dimensions, panic conventions, like, I maybe would feel better if, like, people that worked on SEMCOV… Yeah, exactly. Yeah, exactly.
Alolita Sharma 00:17:21 Exactly.
Ted Young 00:17:22 Grask?
Alolita Sharma 00:17:23 Rusque.
Trask Stalnaker 00:17:25 I think, yeah, I think it would be reasonable to… say, like,
we would want some kind of indication from the project that this is, as Austin said, aligned, or that it's something that we would consider. Like, it doesn't have to be, like, we're saying yes, but…
That we're… like, we haven't really given any positive
Feedback yet on this, like, that,
So it feels a little early…
To be, sort of… it feels like it's creating this…
impression that it's a more project that has been, sort of, reviewed at the project level already.
Austin Parker 00:18:16 Yeah.
Pablo Baeyens 00:18:21 Is there a wording that would…
alleviate those concerns on the blog post. Right now, it says it is a draft proposal, but I don't know if…
you're.
Austin Parker 00:18:31 I mean…
Pablo Baeyens 00:18:32 Just with it being linked at all, or with…
Austin Parker 00:18:36 I think…
Pablo Baeyens 00:18:37 The wording, specifically.
Ted Young 00:18:46 Great.
Hey.
Austin Parker 00:18:49 It's just like, this is one person's thing. This is just a minute test.
Like, this is just one of those things where it's like, okay, you're just doing this, right? Like…
Ted Young 00:19:01 This person, yeah, they're trying to do some product design, analyst work, and there's.
Austin Parker 00:19:06 Right.
Ted Young 00:19:07 By developing this model through talking to people and writing about it and all of this stuff.
Austin Parker 00:19:12 Like, yeah, yeah.
Ted Young 00:19:14 I don't want to discourage someone from doing that.
Austin Parker 00:19:16 No, I don't want to discourage it. I think I… I don't want… To oversell it?
Ted Young 00:19:28 I think a series of blog posts talking about it, referencing it as an issue because it's not even written down yet anywhere.
Yeah, that's maybe a little too soon, but…
Austin Parker 00:19:39 Yeah, I feel like my actual goal here is, like, hey, maybe pump the brakes a little bit, Casper?
And, like…
Ted Young 00:19:48 Right.
Austin Parker 00:19:49 I don't think there is anything wrong with what you are trying to do, what is trying to be done here. I think that, like.
This is a lot of words that impact a lot of people.
Alolita Sharma 00:20:03 Yeah.
Austin Parker 00:20:03 that a lot of people need to review, and right now its canonical source is a 33-page Google Doc.
Alolita Sharma 00:20:11 No, no, and the question is…
Austin Parker 00:20:12 And that would happen.
Ted Young 00:20:13 Gartner called and they want their job back.
Alolita Sharma 00:20:16 I thought I already had the job.
Trask Stalnaker 00:20:23 Maybe ask them, like, as a concrete ask, we could ask them to come to the spec for…
Austin Parker 00:20:30 Yeah, kind of… Yeah, that's a good…
Trask Stalnaker 00:20:34 Yeah, GC.
Ted Young 00:20:37 There's other people who would be interested in doing this work, right? Like, there are other, definitely other product design analysts.
Austin Parker 00:20:43 Bird.
Ted Young 00:20:43 You know, can tell,
Austin Parker 00:20:45 No, I think it's.
Ted Young 00:20:46 So…
Austin Parker 00:20:47 Yeah.
Ted Young 00:20:49 Yeah, but probably we should give them a SIG and a repo where they can stick this stuff, or maybe this is, like…
Developer experience or community… community.
Austin Parker 00:20:59 I mean, I… yeah, like, honestly, maybe, maybe have the… CM Community Management.
do something, I don't know. I think it would be good.
Alolita Sharma 00:21:11 Austin, Austin, to your point, what's the objective here, right? That is, is it to…
convey some kind of measurement to the larger community, vendors and end users included, or what is the measurement? Are we… are we adopting this on every SIG?
Austin Parker 00:21:29 Right, that's… Is it… Right, so my concern is that, like, that's…
It's a lot of stuff that… Watches a lot of people.
And I think just kind of, like, throwing it out there, I mean, like, it's a draft proposal, like, is maybe overselling it a little bit? So, my more actionable… my actionable point on this is just, like, hey, let's maybe pump the brakes a little, a touch here.
on… on this proposal. Like…
Ted Young 00:22:02 Or maybe more on, like, referencing it in a bunch of blog posts.
Austin Parker 00:22:07 I agree.
Ted Young 00:22:08 Let's, like.
Austin Parker 00:22:08 Well, in the proposal, you should keep working on the proposal, but just, like…
Ted Young 00:22:11 But let's not write a whole series of blog posts that reference it.
Austin Parker 00:22:16 Yeah, or like, when you talk about it, it's like, this is something that I am doing, that I would like to… I don't know, like, I just…
Ted Young 00:22:26 Can we get the person a SIG?
As a next step, right? Like, it would be good to have…
Austin Parker 00:22:32 Can I ask her if I'm gonna say hi?
Ted Young 00:22:33 about it, and it's either gonna be us and this person thinking about it, or it could be a group of
Like, people who are interested in it thinking about it, I kind of feel like it would be better.
Alolita Sharma 00:22:43 The second will be better.
Trask Stalnaker 00:22:44 I'd like to see a SIG sort of bless the general idea of it.
Austin Parker 00:22:53 Yeah.
Ted Young 00:22:54 Yeah.
Trask Stalnaker 00:22:55 Because it's such a kind of a… it's like a statement-y thing, it's not like some side project.
Alolita Sharma 00:23:02 That would be…
Trask Stalnaker 00:23:03 okay to have on the blog that is clear to readers that, oh, this is a cool side project. This is kind of like, oh, this is a big…
OpenTelemetry.
Alolita Sharma 00:23:15 Initiative, yes.
Ted Young 00:23:18 Yeah, but there… there… so I feel like we've talked about wanting to have, like, a native instrumentation initiative, and this feels like part of that, right? Like, a good first step is to start to be like, what does the CNCF ecosystem look like?
In terms of telemetry support. What does it even look like, right? And then use that as, like, the springboard for being like, how do we get more things to… like, what would we like it to look like?
That's sort of when I think about us doing our own analysis.
of the ecosystem. Those would be the goals.
But we… that's, like, as a GC, I feel like we're right now trying to be like, let's just get graduated and stabilized and everything, and then we'll think about…
that other stuff, along with Weaver and things that would make it easier for people to not screw it up.
As, like, the next step.
But if other people want to start on that work from…
like, like, how do you even evaluate this stuff kind of framework thing. That's cool.
Trask Stalnaker 00:24:22 Reminds me, Jirassi, of instrumentation score…
Juraci Paixão Kröhling 00:24:30 Which part of it?
Trask Stalnaker 00:24:32 Just the evaluating instrumentation… quality of instrumentation.
Austin Parker 00:24:37 Right, and also, to that specific point, I think…
The lessons learned from instrumentation score, or at least how we started talking about it, means that we should.
Juraci Paixão Kröhling 00:24:48 Yeah, so I think the major lesson learned from my side is just do it, doesn't work.
we've just done it, and then people complained, and then people said, you should not be coming to our CMCF Slack, see CMCF Slack, you don't belong here.
Like… this is in part what triggered me last week, right? But anyway, so…
lessons learned from Instrumentation Square. We try to gather a community and gather opinions about what is good telemetry, what is bad telemetry.
And those opinions are encoded as a… on a repo, on an organization that is open, like, not within any specific
organization.
And the thing is, it wasn't opened as one specific person. Before making it public, we got
People from different companies, like yourself.
Yeah, yeah.
There's zero, and so on.
But those are opinions. There's…
Austin Parker 00:25:47 Right, I don't want this to be re-litigating instrumentation score. My point is simply that for something of this
size and scope, I think it would be good if there was more of a, like.
If more than one person had, you know, had their hands and eyes on this, right?
Before we even go out.
Trask Stalnaker 00:26:06 approach.
Juraci Paixão Kröhling 00:26:07 So… This is a project.
Austin Parker 00:26:08 This is an hotel project proposal. Like, that… I think the actual actionable thing here is, like, hey, great, you need to, like, put this through the project process.
Trask Stalnaker 00:26:17 Yeah.
Juraci Paixão Kröhling 00:26:18 I like that.
So I think… And then they can block.
Trask Stalnaker 00:26:21 They can blog about the… that, hey, here's a project proposal.
Austin Parker 00:26:26 Right.
Trask Stalnaker 00:26:27 As, like, advertising, we do that.
Austin Parker 00:26:29 It can start from a draft, like, this is a great, like, first draft, whatever…
You know, starting point, but, like…
Juraci Paixão Kröhling 00:26:38 So I think there are…
I kind of know some of the content that Casper has created in the past.
And I think he published
this idea of a matrix model before. I think he might even have a KubeCon talk for next KubeCon, or previous KubeCon, I don't know.
So I think…
A lot of this blog post is an opinion from Casper, and this is why it's a blog post.
But I agree with y'all that, you know, this is a little bit more official than a blog post.
It has the potential of being
seen as the opinion of the project, and I think it should not be that.
Austin Parker 00:27:18 Yeah.
Juraci Paixão Kröhling 00:27:19 I don't know, from my side, I… I can relate to some of the blog posts that I published before, like, a lot of them are opinions, and I try to make it clear that it's an opinion at the very beginning, when I think
There might be some confusion.
But I think, this one here might be a little bit too much.
Ted Young 00:27:37 Yeah.
Austin Parker 00:27:39 Well, I mean, you can, if you want to…
Ted Young 00:27:40 publish on his own on, like, the Dash Zero blog or something.
Austin Parker 00:27:44 Right.
Alolita Sharma 00:27:45 Yeah, exactly, exactly.
Austin Parker 00:27:46 Or…
Alolita Sharma 00:27:47 But… That's…
Ted Young 00:27:48 kind of a middle ground, and if he wants to go this direction, I don't think we should say no, we should just say, like, you know, in or out, right? Like, let's go all the way in, make a project, and, like, let's get some…
Austin Parker 00:28:00 Yeah.
Ted Young 00:28:04 Or just go have your opinion somewhere else, and that we don't… we're not gonna, like, complain about you doing that.
Trask Stalnaker 00:28:10 Yeah, I think the project proposal also helps us see if there's enough community interest in something to be…
Push forward, and if not, that's our reason for… Not bringing it in.
Pablo Baeyens 00:28:25 Yep.
To be clear, we not only want him to file a project proposal, we also want some level of interest from people.
Alolita Sharma 00:28:34 Yes.
Pablo Baeyens 00:28:34 here.
Alolita Sharma 00:28:35 Exactly.
Austin Parker 00:28:35 Well, that's what the project proposal gets you, is…
Alolita Sharma 00:28:40 I mean, people have to vote on it, right? At least, and comment.
Ted Young 00:28:43 You need to fill out the staffing section of, like.
Austin Parker 00:28:45 Right, you have to, like, have people…
Pablo Baeyens 00:28:47 Yeah.
Ted Young 00:28:48 Who not from Dash Hero is going to also work? Yeah.
Austin Parker 00:28:51 And I think, I mean, honestly, I think it'd be fine to say, like, oh, I'm, like… I think it's fine to say, like, oh, here's the project proposal, I'm gonna write a blog about the project proposal, and announce that, and get interest that way. Totally fine.
Alolita Sharma 00:29:06 Yep.
Austin Parker 00:29:06 So…
Trask Stalnaker 00:29:07 Yeah, and there's some prior art for that that…
We can point people to. Yeah. We do that.
Austin Parker 00:29:16 Do we wanna move on to the next thing?
The one-line change to the homepage that…
Trask Stalnaker 00:29:26 Was, so who was… Pablo, were you…
taking action on that, I didn't.
Wasn't sure.
Who is… Gonna follow up on that.
Austin Parker 00:29:37 It was Severin. It was Severin.
Alolita Sharma 00:29:39 I thought it was just 7.
Pablo Baeyens 00:29:40 There you go. Okay. Yeah.
Austin Parker 00:29:42 we should… note.
Pablo Baeyens 00:29:44 let him.
Austin Parker 00:29:44 We've put… yeah, we should just, like, put some notes on the thing so that everyone knows.
Trask Stalnaker 00:29:49 I'll put a comment in the GC channel.
Alolita Sharma 00:29:53 Devin, if you're watching this, we're signing everything to you.
Austin Parker 00:29:59 That's what you get for not being here.
He's like, what? The fireworks are, yeah, good… good timing.
Apple.
Alolita Sharma 00:30:08 Yeah.
Marylia Gutierrez 00:30:08 The reaction was just, yeah.
Austin Parker 00:30:18 So… Drafts, home… homepage copy changes.
Juraci Paixão Kröhling 00:30:24 Copy changes, so…
Severin asked me to, bring it up here, mainly to, you know, get your… your attentions.
To this one PR.
this is… Draft mode, because it's only me in one afternoon trying to change text.
Going into a different direction.
I'm not a copywriter, I'm not a marketing writer, or anything like that.
But I think it is… Anyway, I opened the draft and asked people from the comms to…
polish it, make it better, and I think it is now at a point where Seven is asking you all to take a look and see if that's a good direction to go.
If you are interested in providing feedback, go there, make a comment.
Otherwise, ComZ will be able to take it over.
Austin Parker 00:31:15 I don't think we can call it a standard.
My recollection from this… maybe… maybe the CNCF has changed their ways in the ensuing 5 years.
Ted Young 00:31:32 Them complain about that in, like.
Morgan McLean 00:31:34 Yeah, I feel like.
Alolita Sharma 00:31:35 But they certainly complained about it in the past.
Ted Young 00:31:39 Very beginning, they came.
Morgan McLean 00:31:40 Yeah, I think it's big enough that probably we're not gonna get a whole lot of pushback on that.
Austin Parker 00:31:45 Yeah.
I mean, Kubernetes does not call itself a standard on its page.
Ted Young 00:31:51 I think we're different than.
Morgan McLean 00:31:52 I think it's different, yeah.
Austin Parker 00:31:53 It's different. True. No, that's true.
I'm just…
Alolita Sharma 00:31:57 I think they will… they have objected to it even in recent times.
Austin Parker 00:32:04 I do…
Alolita Sharma 00:32:05 Standard.
Austin Parker 00:32:06 I think the… I… I just…
I just know that people are gonna get mad. Like, the open source people are gonna get mad, because the CNCF is not a standards body.
Alolita Sharma 00:32:22 Yeah. And…
Austin Parker 00:32:29 I'm not saying we should or shouldn't… I'm not saying we shouldn't do it.
Morgan McLean 00:32:31 You're just saying expect some pushback.
Austin Parker 00:32:33 I'm just saying that, like… we should A expect pushback, and B, probably… Like, clear it with… CNCF Marketing.
Morgan McLean 00:32:46 Yes.
Ted Young 00:32:51 Thesaurus says we could call ourselves a norm, Or a barometer.
Austin Parker 00:32:57 Oh, barometer!
Marylia Gutierrez 00:32:59 When I would say, like, THE open standard, you change to, like, an open standard, where just…
None of them.
No, the word standard is what they get a little…
Alolita Sharma 00:33:12 And they opened.
Austin Parker 00:33:12 I'm sorry.
Pablo Baeyens 00:33:13 They standardized, so, like, Open and standardized telemetry.
Alolita Sharma 00:33:19 You could probably say…
Ted Young 00:33:21 A yardstick, and then we would piss off everyone.
Alolita Sharma 00:33:24 I mean, literally.
Austin Parker 00:33:25 The meter stick for open source observability.
Ted Young 00:33:30 The standard yardstick is what we should… Say we are.
Austin Parker 00:33:35 The SI… the SI for, telemetry is…
Marylia Gutierrez 00:33:40 We're just gonna use another, like, language. We ran in Portuguese. They're like, I'm not using standard, I'm using Padreon, which is a completely different.
Austin Parker 00:33:48 There you go, yeah.
Ted Young 00:33:51 The Padron? The Padron of…
Marylia Gutierrez 00:33:53 limited.
Alolita Sharma 00:33:58 to confuse them, yes.
Austin Parker 00:34:01 I mean, our… Do we feel strongly enough that we want to, like, fight for the word standard?
And marketing copy.
Alolita Sharma 00:34:12 Well, you know, the prom community might go and object to you. It's like, what? We're the standard.
Austin Parker 00:34:20 I mean, that's… that's… that's… that's one thing we should consider.
Morgan McLean 00:34:31 The foundation for telemetry, which Pablo just posted, could be good.
Alolita Sharma 00:34:35 Yeah, funny?
Austin Parker 00:34:36 I mean, I think Foundation…
Ted Young 00:34:38 Yeah, I like that.
Alolita Sharma 00:34:40 Yeah?
That's…
Juraci Paixão Kröhling 00:34:42 So, can I… can I ask you all to make your comments there on the PR?
Alolita Sharma 00:34:46 Yes, yes.
Juraci Paixão Kröhling 00:34:47 So that, you know, this.
Alolita Sharma 00:34:48 That's good.
Juraci Paixão Kröhling 00:34:49 happens there or not here.
Austin Parker 00:34:50 That's fine, I just wanted to… yeah, I just wanted to get a temp track to see, because if we're going to change it to something that is, like…
going to cause problems that I would rather go have that conversation with the people that are…
I would rather go inoculate people now rather than later, but if we are not wedded to the word standard, then I think we can just have this conversation in the PR comments.
So…
Juraci Paixão Kröhling 00:35:14 I think… whenever we go to KubeCon and we have a talk, like.
We… we typically say they're at the… at the podium, like, at the… the…
stage, we say, you know, open telemetry is a de facto standard for telemetry. Like, we say that all the time. That's the message that we get. We write that on blog posts and things like that. I think this is what the hero should say in our page. If anybody has any problems, they can come to us and ask, and then we can change.
Austin Parker 00:35:41 Well…
Juraci Paixão Kröhling 00:35:42 defect.
Austin Parker 00:35:43 standard for open source observer. Right, there's a difference… there is a difference between saying the open standard for software telemetry and the de facto… the open de facto standard, right?
Juraci Paixão Kröhling 00:35:57 So, we can start with this standard, and then if they complain, we can change to the de facto standard. I mean…
Let's make it simple, let's make it memorable, if, like, there were de facto
We can add it later, if needed.
Ted Young 00:36:14 I'm with you, Jurassi, I'm willing… I'm willing to see if anyone cares.
Morgan McLean 00:36:17 Yeah.
We might be overthinking ourselves here.
Ted Young 00:36:20 I feel like we could take the heat and just change the word if it turns out people truly care.
Morgan McLean 00:36:25 This is very different than, like, 2019, when the project was getting started and had no implementation or users or anything.
I'm curious if we actually get a reaction or not. I'm not saying we won't, I just…
It's possible we won't, I just.
Ted Young 00:36:39 I'm curious now, I want to perform the.
Trask Stalnaker 00:36:42 You wanna test?
Austin Parker 00:36:43 What if we ate…
Alolita Sharma 00:36:46 Raven Rouse.
Morgan McLean 00:36:47 I have a checkpoint here.
Austin Parker 00:36:50 We should install water.
Ted Young 00:36:53 We need to let people know that we're, like, stabilizing and, like, doing all this good shit, so we need attention right now, and this is the best way to get it. Yeah. Start totally, like, spur…
Alolita Sharma 00:37:03 Start a flame war.
Ted Young 00:37:04 And then start plugging all the shit that we're up to.
Austin Parker 00:37:08 get a bunch of people on Mastodon and Lobsters to get really annoyed at us, and the CNCF by proxy.
those IETF people.
Alolita Sharma 00:37:18 Oh, yeah, exactly.
Ted Young 00:37:19 to help us, like, get the semantic conventions updated and all of the instrumentation, yes.
Austin Parker 00:37:25 Look, actually working on something would take valuable time away from posting about what other people are doing, Ted.
Juraci Paixão Kröhling 00:37:34 So… Yeah, leave your comments there, please. But it's also…
get your attention, it's not only the hero part, right?
Austin Parker 00:37:43 Yeah, no, I…
Juraci Paixão Kröhling 00:37:45 Right.
Austin Parker 00:37:45 I was…
Alolita Sharma 00:37:46 Yeah, the rest of it just looks okay.
Marylia Gutierrez 00:37:49 You want to remove from drafts, because then people, if they think they're good, they can actually approve.
Juraci Paixão Kröhling 00:37:54 So…
I opened the PR with my thoughts, and I really don't have the time to get it through. It's just, like, the initial…
the initial… Sparkle to make it moving.
To get it moving, but I hope the comms folks are gonna take the lead, and I was actually hoping that they would already have forged my PR,
Into their own PRs.
Yeah, that's why it's…
Austin Parker 00:38:18 I mean.
Marylia Gutierrez 00:38:19 Yeah, I would say, because, a few of them were, like, taking a step back for something, so a few of the others, we are having to take ownership of a couple things, so I'm not sure if people have, like, a lot of.
Juraci Paixão Kröhling 00:38:32 Oh, but the other…
Marylia Gutierrez 00:38:33 Yeah.
Juraci Paixão Kröhling 00:38:34 So, I think in there, both,
both, Charlene, so that's, Patrice,
Austin Parker 00:38:44 Previously, yeah.
Juraci Paixão Kröhling 00:38:45 And, and, fabricio, mentioned that they could take it over.
Austin Parker 00:38:52 Yeah, I mean, I… Given that this is, like, the hero stuff, I would be… I will…
I will fork this… do some wordsmithing and, drive it. Does that work for folks?
Alolita Sharma 00:39:11 Yeah, totally.
Austin Parker 00:39:12 I… I'm… I mean, I'm still a maintainer on comms, so…
Alolita Sharma 00:39:19 That'd be awesome. Awesome.
Austin Parker 00:39:22 And also Ideally, that it will…
I don't know. I feel like it's like, oh, nobody can, you know, it just makes it…
Gives us a place the buck stops for this sort of stuff, right?
But I can… I can definitely do that.
Times…
Morgan McLean 00:39:54 The only other question I had about it is, do we want to specify it as software telemetry, or just keep it as telemetry?
Alolita Sharma 00:40:00 Yeah, exactly.
Morgan McLean 00:40:01 Obviously, it's generated using software, but, like, I have customers who use OpenTelemetry to.
Austin Parker 00:40:06 Yeah, no.
Ted Young 00:40:06 times in horse races.
Alolita Sharma 00:40:08 Yes.
Juraci Paixão Kröhling 00:40:09 Though…
Ted Young 00:40:09 Yeah.
Juraci Paixão Kröhling 00:40:10 I… so, my personal experience is, whenever you use the word telemetry, at least in Germany, people make the connection to car telemetry.
Art elements.
Ted Young 00:40:23 Our telemetry?
Juraci Paixão Kröhling 00:40:25 Really?
Morgan McLean 00:40:25 I feel like that's very regional.
Alolita Sharma 00:40:27 That's fair.
Juraci Paixão Kröhling 00:40:28 It might be, it might be.
Austin Parker 00:40:29 Yeah, I agree.
Juraci Paixão Kröhling 00:40:30 that I spent, like, 40 minutes pitching over the garden to somebody, only to have them, think that, oh, this is about car telemetry, right? And this is not it, no.
Morgan McLean 00:40:39 Like your integrator with Mercedes or something, yeah.
Marylia Gutierrez 00:40:42 Just, like, telemetry, and put, like, notes. If you are from Germany, we are talking about…
Alolita Sharma 00:40:50 context.
Austin Parker 00:40:52 Yeah, I think the American and maybe Canadian valence is a lot more towards, people you think user analytics.
Morgan McLean 00:41:00 Yeah, that's… yeah, that's my fear by.
Ted Young 00:41:03 They're gonna think anything, right?
Morgan McLean 00:41:06 I was gonna say, that every time it comes up on Hacker News, you see the people.
Austin Parker 00:41:08 I would honestly probably just say the open standard for observability.
Juraci Paixão Kröhling 00:41:15 So, I was explicitly going away from the word observability, because we don't define SLOs, we don't define alerts, we don't define dashboards, like, this is not.
Austin Parker 00:41:26 The open foundation for… the open foundation for observability… for observability data.
Ted Young 00:41:31 Open standard for telemetry, please.
Juraci Paixão Kröhling 00:41:34 Yeah, sure, we'll figure it out.
Ted Young 00:41:37 We are! We're standard for telemetry. Jurassi, 100%. Like, that's… that's correct, what you're trying to say there. I think we should just say it, because that's what we say everywhere, and…
Austin Parker 00:41:48 Yeah.
Ted Young 00:41:49 Get out with the CNCF or whoever the hell has a problem with that.
Because, like…
Juraci Paixão Kröhling 00:41:54 My concern with observability is, it…
it is kind of like telling everybody, like, we do anything. And when you say… when you tell people that we do anything, people just get confused, like, oh, what do you mean, you do anything? Can you make me a sandwich? No, that I cannot do. And the same for observability, like, can you do alerts? No, we cannot. Can you do data storage? No, we cannot.
It is transport.
Austin Parker 00:42:19 Not for horses.
That's part of everybody.
Ted Young 00:42:23 I definitely think…
Juraci Paixão Kröhling 00:42:24 You can measure velocity.
Ted Young 00:42:27 Like, it's literally the name of the project, right?
Austin Parker 00:42:30 No, that's fair.
let's not use this word, because no one knows what it means, like… No, I mean, I… yeah, I… I will sit down and do some wordsmithing, and…
I will have a… Forking this PR up today.
Alolita Sharma 00:42:46 Sounds good.
Cool.
Ted Young 00:42:54 Alright.
Austin Parker 00:42:54 And there we go…
Marylia Gutierrez 00:42:56 So yeah, just kind of like an update, just to see if there's any objections, but, both me and Ted were working kind of like a…
reports of Hotel Unplug, but the idea is to actually
bring this back to the community, so it's not just for the people who attended. So, the idea is to put on the community repo, have, like, for example, one folder to be, like, Hotel Unplug, where we can put, like, some guidelines for the next people that wanna, organize one.
And also have a session that… so I did, like, a summary for all the sessions that happen, removing anything that would… could consider, like, oh, I can know who said the thing, kind of thing, so I have, like, a short summary for each one.
So the idea is to also put those ones, just to see what community is talking about. So yeah, working on this, just to see if any objections, or if we can just continue going ahead with it.
Alolita Sharma 00:43:51 I think it's a great idea, Marilla, because it'll be very helpful for folks who are going to do it again.
Ted Young 00:44:02 Yeah.
Marylia Gutierrez 00:44:02 Yeah.
Ted Young 00:44:04 Just, like, basically a how-to-unplug doc.
And also, like, based on…
what we learn, try to figure out how to do the next one. Also, who's going to throw the next one is a question. I think Grafana would be fine.
holding down the next one attached to Fostum, we're totally fine doing this one again next year. Some people wanted to throw one in, like, Canada, Vancouver would be awesome, but…
Alolita Sharma 00:44:34 Vancouver, Vancouver.
Ted Young 00:44:35 We want this to be a community…
we want to kind of pass the hat around, so, like, we actually, like, actively don't want, as putting my Grafana hat on, like, we don't want to just become the default people throwing it all the time, because that'll…
settled.
screwed up.
We are looking at…
Another… What are they called? Trying to find a way to get a bank account, basically. And there are other open source, foundation-like things that are a little more oriented towards… we will do that part for you.
it's a little ironic to go outside of the CNCF, but, like, that's just…
The one… one piece of feedback we got was, like.
When vendors decided they didn't want to sponsor it anymore, for whatever internal reason, this was never actually the reason, but they would come back to us and say, we're not sponsoring this because this is being, hosted by another vendor, and we're not comfortable with that situation.
This happened multiple times, and it was bullshit every time. Every time it was like, we have some internal reason, and, like, but this is, like, a convenient reason.
Morgan McLean 00:45:52 My only reason was lack of budget.
Ted Young 00:45:54 Great.
Austin Parker 00:45:55 Let me…
Ted Young 00:45:55 Right, this was for people who got far enough along that they decided to move back out later.
Austin Parker 00:46:00 It's just like, I wanna…
Ted Young 00:46:01 Like, some nonsense.
Austin Parker 00:46:04 I do want to say, like, part of the reason that it took so long to get to the point of
like, part of the reason it took so long to get to the point of even having… getting there, right? Basically, having it be a Grafana thing added friction.
Like, I… handing out…
Ted Young 00:46:25 Like, give me a break.
Austin Parker 00:46:28 I'm not in marketing! I don't have… I can't… like, I can control what I spend on my personal… on my corporate credit card, and that's it, right? But, like…
trying, like, this… I'm saying, and this is Honeycomb, which is, you know, a pretty small place where I know every single person personally that needs to, like, go through this, but…
Blake… I can go and say, hey, events team, we should sponsor this, and…
And they're like, oh yeah, sure. And then it has to go in front of, like, all these other people, and then someone sees… and then it comes up in a meeting on a spreadsheet, and someone goes to the thing and says, Grafana, like… right? Like, it adds friction.
And that fri- and friction… is bad.
Ted Young 00:47:17 Yeah.
Austin Parker 00:47:18 like.
Ted Young 00:47:18 We totally agree.
Austin Parker 00:47:20 We wouldn't have pulled out if we had already paid for it.
And… but we didn't already pay for it because it took so long to get to the point of wanting to pay for it because of the friction.
from it being a Grafana thing.
I know, you know, we all know that it's bullshit, yes, and we know that, like.
Okay, so, so, right, but it's an actual issue, is what I'm saying.
Ted Young 00:47:46 Long story short, two pieces of feedback that are, like, you know, things we have to figure out for the next time is how we actually sort out the schedule we need to do in advance, because that was, like, some cowboy shit that, you know, we were able to pull off, but I'm like, I would not wish…
that on other organizers. We need something more organized. If it's gonna be a one-day event in particular, we just can't spend a lot of time
corralling the sessions together, so that needs to be a little more of, like, an app people use or something. Anyways, we gotta figure that out, we could probably build it on top of Votel. The other thing is, like, we want to take another stab at finding some way to get a bank account. For this very reason, one is that
genuine friction, right? Like, whether it's legit or not, this was, like, absolutely a thing we got from a couple of different sponsors, just friction around that. And if we could find a more neutral place to house the bank account, and thus, you know, like, what we were putting money into and pulling it from.
That would be…
Morgan McLean 00:48:53 can't use CNCF as the neutral place, because they're gonna get…
Ted Young 00:48:58 I love kids.
Morgan McLean 00:48:58 BigCon, and, you know.
Ted Young 00:49:00 Because we're just gonna end up with Hotel Community Day Part 2. Fair enough.
Alolita Sharma 00:49:04 Eggs, eggs.
Austin Parker 00:49:06 What do you mean?
Morgan McLean 00:49:06 What happened? Yeah, that's what I thought.
Austin Parker 00:49:11 Counterpoint, we know how…
Ted Young 00:49:12 Linda would be very nice. That would be nice.
Austin Parker 00:49:15 Counterpart, we now have 3 people that can go and, like, work on this problem, right?
Morgan McLean 00:49:19 Yep.
Austin Parker 00:49:20 like, we can tell Adriana and Reese.
Ted Young 00:49:23 Yeah.
Austin Parker 00:49:24 to go…
Ted Young 00:49:25 There are other organizations that do more just this for open source projects.
Austin Parker 00:49:31 Right, like…
Ted Young 00:49:32 We have some community thing, and we want to throw events, and this foundation houses that bank account for you.
Austin Parker 00:49:38 Yeah.
Ted Young 00:49:39 And that's, like, all they do.
We want to look into those or something. It would also make it a lot more turnkey to throw these things in the future if it wasn't, like, a different event staff and bank account and whatever, right? Like, if we want to just throw it at the same venue at Fostom again next year, right? Like, that works a lot better if…
Like, anyways.
So…
Austin Parker 00:50:03 Yeah, or I'll…
Ted Young 00:50:03 Those are the next steps that we want to figure out with Unplugged.
Austin Parker 00:50:07 I was also gonna say, like, another option would be…
If there's event companies or, like, event organizer peoples that… would do…
Like, do stuff at cost, right?
Basically, like, hey, You get, you know…
you organize it, you run the, you know, you have the fin… you have, like, the financial side of it, you have the bank account so that people can, like, send money for sponsorship, and you also, like, do, like, some of the logistical stuff in terms of, like, booking the venue, and da-da-da-da-da, and you get…
you know, You get to recoup your costs plus whatever from the sponsorship fees?
Ted Young 00:50:55 Yeah, I don't.
Austin Parker 00:50:56 Like, right, there are a bunch of options that I think we can explore.
But I think… It'll be on…
Adriana and Reece to, like, explore those.
Ted Young 00:51:08 Well, anyways, we've got a… I've been doing a lot of work internally to, like, get all the feedback.
Marilla's been helping me with that. We're gonna turn that into a blog post and a how-to guide as our next steps. Grafana's totally fine if nothing else changes. We will throw the next unplug
Same time next year, and if we can get it together to throw more of these, or in a more neutral fashion between now and then, that would be great.
Juraci Paixão Kröhling 00:51:37 How many people did we have?
Oh, you need?
Austin Parker 00:51:40 Help.
Ted Young 00:51:41 So it was about 120, 120 attendees?
Juraci Paixão Kröhling 00:51:45 So, this is not much bigger than a meetup, right? So, I mean… Yeah.
We typically have 40, 50 people at meetups here in Berlin for hotel night.
I guess the question is… and most of the time, we can get the venue for free, and companies are happy to sponsor even the food, given that we have, I don't know, two or three CNSF ambassadors as part of the OTL in general. We have
500 bucks for food, which… I mean, for 200 people, I mean, it doesn't have to have catering, it could be a meetup-like scenario, I suppose. I guess the point that I'm trying to make is.
does it have to have a budget? Does it have to have, like, a formal, like, sponsors and things like that? Can't we not tap into users of hotel to provide a venue, plus everybody brings something to drink and to eat?
Marylia Gutierrez 00:52:38 I think the difference… Meetup is, like, a one-two hour thing, this is all.
Ted Young 00:52:43 that.
Marylia Gutierrez 00:52:43 Entire day thing? Yeah, you can.
Austin Parker 00:52:45 Yeah.
Ted Young 00:52:46 Without catering at an all-day event, you… people will leave for lunch and they won't come back. Like, trying to do it as, like, a tight one-dayer, it's much better. Where you could make it cheaper is if we had a company be like, we're just… you can use a floor of our office.
Alolita Sharma 00:53:00 Yeah, exactly.
Morgan McLean 00:53:01 I think it's worth pursuing.
Ted Young 00:53:03 You know, that's…
Morgan McLean 00:53:05 get, like, pizza delivered or something, like, that would totally work.
I think that's really worth looking into.
Alolita Sharma 00:53:10 Yeah, yeah, it is, it is, it is, because there are menus.
Ted Young 00:53:14 Making it cheaper would be totally clutch. Yeah.
Juraci Paixão Kröhling 00:53:17 So, I'm doing something like that next, in a couple of weeks' time in Brazil. So, I'm hosting a hotel night, but in the afternoon, in Sao Paulo for the whole afternoon.
open to the public, and free, no tickets being sold, anything like that. And a bank in Brazil is sponsoring the place, and the food, and the beverages, right?
so far, we have already, I think, quite a good number of people, right? So, it's doable, I suppose.
Austin Parker 00:53:46 Yeah, the one…
The one point I'll make about the… yeah, the one point I'll make about, like, the… just have, get someone to give you a floor of their office all day.
You still have to deal with registration, you still have to deal with all these things, right?
Alolita Sharma 00:53:58 And, and security and stuff.
Austin Parker 00:54:01 You're right, like, the biggest thing with
Yeah. Doing it at a place is…
like, hell, Amazon, you know, you can do an all-day event in an Amazon office, right? And they'll usually even give you food,
But, like, you have to have everyone's names ahead of time, and they all have to go through security, and they can't leave.
Alolita Sharma 00:54:22 And if they leave, you can't get back in, you know?
Morgan McLean 00:54:25 It depends on the building, because, like, some Amazon and Google and, I think Microsoft offices, I don't think this is super common, some of them do have large conference areas that are outside of the security boundary.
Austin Parker 00:54:35 Oh, okay, well… Right, like, Google New York has this, Google Kirkland has this, I know Microsoft has a handful. Now, they might not be in the cities we want, who knows if we get access, but they do… they do actually have facilities specifically for events like this.
Alolita Sharma 00:54:46 No, that's true, Google does.
Austin Parker 00:54:47 Microsoft does. Yeah.
Morgan McLean 00:54:49 You will definitely notice.
Austin Parker 00:54:50 I don't know…
Ted Young 00:54:51 Something…
Austin Parker 00:54:52 I've never been to Amazon one, like that.
Morgan McLean 00:54:54 Yeah, I don't know if Amazon does, yeah.
Alolita Sharma 00:54:56 I think it's on…
Ted Young 00:54:57 Let's pull off an all-day event that doesn't have, like, actual event organizers trying to, like, hold the whole thing down, right? We may not need money, but you're definitely gonna need our group organizers.
Austin Parker 00:55:09 I'm in people. Yeah, yeah.
Ted Young 00:55:10 with all of that, whatever the hell it is. And the more free it is, probably the more time will be on those organizers' plate to…
Morgan McLean 00:55:17 Yeah, yeah.
Alolita Sharma 00:55:18 That's right, that's true.
Morgan McLean 00:55:19 That's true.
Ted Young 00:55:20 Whether that's our community organizers doing that, or we're passing the hat around for those people, That…
Juraci Paixão Kröhling 00:55:26 Cool.
Ted Young 00:55:27 We're out.
Austin Parker 00:55:28 two…
Ted Young 00:55:28 But I do think if we get it more automated, we could also have a more chopped-down one, like what you're doing, Jurassi, like an afternoon or an evening, but more like if you wanted to add some, like, unconference-y level of self-organizing. I think that's the thing we could give
If we wanted to make it cheap and self-serve, it would be to do what you're saying, which is, like, find a way to make an even shorter version of this that you could run more, actually, like, a meetup.
Then it would be, like, super easy to throw a, like, one or two round version of this thing.
Because you wouldn't have to.
Juraci Paixão Kröhling 00:56:04 Which is quite easy to do. Like, I spend, I don't know, at most one hour organizing every hotel night. Typically, like, registration is taken care of by the platform that the CNCF gives.
Food, again, the venues typically provide. If they don't, I get $150 for pizzas from the CNCF as an ambassador. Like, it's easy to do.
Ted Young 00:56:26 I would love more meetups.
Juraci Paixão Kröhling 00:56:28 Yeah. Like…
Ted Young 00:56:28 Right, you're describing… The other thing we can do is just regular old meetups.
Austin Parker 00:56:32 I think meetups are great. I think there's a difference between a meetup and an unconference.
Like, I agree with Ted, like, these are different levels. This is a lot bigger.
Ted Young 00:56:40 Here's the thing I'll say, and I wish we had more time, but, this year is, like.
doubly dead.
for CNCF stuff in North America, because they had already booked everything out in, like, unpopular places in the United States. It's frickin' Minneapolis for…
Alolita Sharma 00:57:01 Oh, exactly.
Ted Young 00:57:02 Even observability dead on arrival, right? Like, Minneapolis, and then Salt Lake City for, like, KubeCon NA. And, like, that was an unpopular venue even before all of the nonsense, just because, like, Salt Lake doesn't…
Like, that… they already had lower than normal attendance just because it wasn't somewhere cool. And now, like, it's that times…
You might get arrested at the border or some weird shit.
Alolita Sharma 00:57:31 Yeah, exactly.
Ted Young 00:57:33 and people were asking for, like, I want a two-day hotel unplugged.
And so it's like… Maybe next year as well, but it's almost like…
Alolita Sharma 00:57:43 Canada.
Ted Young 00:57:44 Through a two-day, like, un-conference anywhere in Canada this year, like, everyone would come to it.
Alolita Sharma 00:57:50 Would be there, yes.
Ted Young 00:57:52 There's just, like, nothing else going on that's very… like, no one's throwing anything in Canada. Monotorama's dead.
Alolita Sharma 00:57:59 Yeah. Like…
Ted Young 00:58:00 Like, there's, like, kind of, like, a weird gap.
on the North America side.
Alolita Sharma 00:58:05 No, no, we should totally do that, for sure.
Ted Young 00:58:07 But I don't think anyone has it in them to try to, like, rapidly get something together for, like, June or July. Anyways…
Austin Parker 00:58:14 Yeah, I certainly don't. I… yeah, I just wanted a quick…
update, touch base on the community manager transition. So, I, talked to…
Reece and Adriana and Gulia, and they are getting crack-a-lackin'. One of the things I've asked them to do is to present a new proposal for
Reimagining the community manager function, and, like, expanding it, and also asked them to figure out what sort of cadence they would like.
to have report backs to the GC, something that I would like from us to the group is figure out
How frequently would we like to talk to them synchronously?
Monthly, quarterly?
So, if we can just have that discussion in… we can have it async, but, we should have that discussion.
Alolita Sharma 00:59:08 Yeah, for sure.
Hmm.
I mean, quarterly for sure, but monthly, if they.
Austin Parker 00:59:15 Right, it's mostly a question of, like, do… is quarterly fine, or do we want to do monthly?
Morgan McLean 00:59:22 Probably monthly? But we can talk about it async.
Austin Parker 00:59:25 Yes.
Morgan McLean 00:59:26 Yep.
Austin Parker 00:59:29 That's all I have on note.
Ted Young 00:59:32 Alright.
In Slack, just FYI, I've been trying to reschedule Merle to come… Merle Kryance to come talk to us about Apache Foundation.
Alolita Sharma 00:59:41 In fact, she worked at the Panshee Foundation forever.
Ted Young 00:59:44 They've encountered a lot of the same stuff we deal with, so…
But, getting exactly this time is a little hard. If people could meet 30 minutes before or after next week, or on Thursday instead, there's a little slack poll.
Alolita Sharma 01:00:01 just go click the button. Okay, good.
Yeah, right is awesome.
Austin Parker 01:00:08 Alrighty.
Ted Young 01:00:10 Excellent.
Alolita Sharma 01:00:10 Right on time. Thank you, everyone. Thanks, folks.
Marylia Gutierrez 01:00:13 Bye.
Trask Stalnaker 01:00:13 She had moved. Bye.
