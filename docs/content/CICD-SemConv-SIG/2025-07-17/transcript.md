SIG: CI/CD SemConv SIG
Date: 2025-07-17
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/4jaqknW3m-MrCd-9vCOjvYXmOe6hr9vfcSVbs1JOXq3XMgNsixvuB1qJiozEL59f.OcNCIYHqmfyUBtgm
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 00:41 Good day.
**Martin Costello** 00:44 Hey? How's it going.
**Adriel Perkins** 00:46 Good! How are you?
**Martin Costello** 00:47 I'm good. Thank you.
**Adriel Perkins** 00:49 Good to hear.
Give everybody else a couple more minutes, but it might just be us morning this morning. This time is proven to be in the last few months. It's it's proven to be not a great time. So we've got a poll going, you know, which you've probably seen in on phase 2, we're gonna we're gonna launch with a new time.
**Martin Costello** 02:07 Okay, yeah. Cause like, I haven't been to every slot since the last one I attend I attended and you were here. But there's a couple of times. I popped in for 5 min, and I was in the only person here, and then left again.
**Adriel Perkins** 02:22 Yep, yep.
oh, thank you for popping in. Sorry that you were the only person here, though. Hope hopefully this new time. With phase. 2 works out better and more folks are able to join.
**Martin Costello** 02:36 Yeah. No worries.
**Dotan Horovits** 02:38 Hey, everyone.
**Adriel Perkins** 02:40 Hey? Good day!
**Dotan Horovits** 02:42 Adrio and Martin.
**Martin Costello** 02:44 Hi.
**Dotan Horovits** 02:54 I was also late last time, and by the time, like I had 15 min late, and when I was joining it was already over. So I guess whoever joined already gave up so miss, that one.
**Adriel Perkins** 03:07 No worries. I was out that day. I forgot to mention it.
Alright. We don't really have much. I started working on cleaning up a little bit of the board gonna clean up even more.
I figure I guess the one update the one key update that I that I have with regards to some of the work that's been cleaned up is the supplementary guidance for environment, variable context, propagation and the specification has been merged.
and that enables sdks to support or support to be added to the to the SDK libraries. Now, there's a couple items that were mentioned on the merger that that the community would like to see.
The spec folks sent it over to me. So I'm gonna take a look at those. But I'm gonna kind of put those in planning for, I guess phase 2, even if I start on them earlier than that.
That's really the only update other than cleaning this up so that we can actually make a formal proposal for phase 2.
I hope to have that pull request up in the next week or 2, that's all I got did y'all have anything in specific? Y'all wanted to talk about? Oh, I got one more thing sorry real quick christoph has had some pull requests that have been open.
Feel free to to comment on them. I think his last one just got. I just approved his his last one yesterday, which was metric supplementary guidance in the simcom repo or it was around an info metric. But yeah. Feel free to review any of those Prs and now, that's it, that's all I got.
**Dotan Horovits** 05:22 Sorry, Adriel. I I got kicked off the thing. So just to make sure what's the ask what to review. I just joined the the very last part. Sorry, sorry.
**Adriel Perkins** 05:30 No, no, you're good. I was just saying that there are, some, I think, couple of Prs from Christoph and the simcom repo feel free to give them a review.
Yeah, okay.
But other than that, I think we're we're gonna be trying to put up a a pull request for phase 2. Proposal in the next week or 2.
**Dotan Horovits** 05:54 Cool.
Let me know when you want to iterate over that, or how you want to go about that.
**Adriel Perkins** 06:01 Yeah, absolutely.
**Dotan Horovits** 06:03 I'll be away next week for Kcd. Munich, but after that I should be having a bit more time to to look into that.
**Adriel Perkins** 06:14 Okay. Cool.
**Dotan Horovits** 06:22 Anyone else the Martin, you're you're not a regular here, so I'd be happy to hear what's what's on your mind
**Martin Costello** 06:32 Yeah, this. This is only the second one I've come to where there's been other people here.
But ma, mainly. I'm just here of an interest to the Cicd space. I did chat with Adriel the 1st time I joined, and we chatted a few bits pieces he gave me, like the the elevator pitch of things. I work in Grafana. So we we get involved in lots of the hotel space, various bits and pieces. And see, I'm just joining. See if there's anything relevant I can do to help contribute here. I think I mentioned to Andrew last time about how I mostly work in the with.net and like at some point in the future, maybe helping out getting like things like the.net test runner like lighting up in the appropriate way when it's used in Cicda tracing for open telemetry. And what have you? I I did ask some engineers at Microsoft if it was something they looked at at all, and the short answer was, no, it's not a thing they've done any research into yet. So so.
**Dotan Horovits** 07:48 That's amazing, actually, because we we don't have too many that come from the net ecosystem. So it'd be great to tap into that just curious when you talk to them. Were they even aware of the existence of the semantic conventions, the specification effort around that anything of the likes, or that, were they even not aware of that.
**Martin Costello** 08:10 If I remember correctly, it was. They were aware that there was work happening, but they hadn't sort of done anything concrete to do with it.
**Dotan Horovits** 08:25 Okay. So sounds like, even basic awareness could be beneficial for them to even get Matt relaying the the elevator pitch and and things like that that Adrian probably did the best. So any opportunity, whether through you, or if they want to join, or or any other way that would help them get acquainted with this, and see how how it translates the things that may be relevant for them. That'd be that'd be cool.
**Martin Costello** 08:57 Yeah, sure, I think I think at this stage I'll just sort of join these meetings, absorb the information.
see what's relevant. And then, if it gets to a point where it's sort of maybe prototype proof of concept type level. Then at that point, like mope, I could open an issue on what the relevant.net repo. Try and get some engagement on where they might want to go with it. If they have something built in.
**Dotan Horovits** 09:26 Nice.
I know there's been quite a bit of work around the.net aspire stack with regards to the sort of cloud native observability, the auto integration.
and that part. And I don't know if it's something that you had a chance to to be involved with or have a look at. But this is actually something that would be also maybe good. Another compelling area within the.net sphere that.
**Martin Costello** 09:56 Yeah, I I use.net as by myself, to do like sort of local observability for web stuff.
**Dotan Horovits** 10:06 Okay.
so I don't know again, if you if you know folks from that area that you want to introduce to the Sig.
if they if they're interested in hearing more, and maybe look into that because I know for them it was really a focus area, the adoption and and con compatibility with hotel in general. So sounds like it also may align with with their goals in general, and that would be easy.
**Martin Costello** 10:37 Yeah, sure, I'll keep an ear out for where it might be relevant to chat to people there.
**Dotan Horovits** 10:45 Great.
So anything else that anyone wants to bring up on the to the discussion.
**Adriel Perkins** 10:59 I don't have anything.
**Dotan Horovits** 11:01 Okay, I can maybe just share briefly that I came back from from open source Summit, North America.
and it was another opportunity to to talk to the community there, and just saying, If if anyone, primarily you, Adriel, if anyone contacts or has questions in in that context. And just so you'd know if it's coming from from that direction hopefully to to bring in some interesting discussions. So.
**Adriel Perkins** 11:40 Cool thanks for the heads up.
**Dotan Horovits** 11:42 Yeah. Yeah. Will any of you, by the way, be at the Open Source Summit, Europe by any chance?
That's next week, like end of August.
**Martin Costello** 11:52 No, I won't know.
**Dotan Horovits** 11:54 Okay.
**Adriel Perkins** 11:55 Me, either.
**Dotan Horovits** 11:55 For you. It's a bit of a schlep. Yeah, I know traveling again across the pond. But yeah, and I I hope to be there. So again, hoping to touch base with the with the community. And I'll try and see more interesting discussions that could could be beneficial, for that actually should ask Dan if he's going to be there, if he's flying over, and then, because for him it's a much shorter flight.
there would be an opportunity to discuss with him as well, and get his feedback, and also with regards to the phase 2 and everything. So.
**Adriel Perkins** 12:36 Cool.
Yeah, my next plan conference is Kubecon, North America. So that's not some November.
**Dotan Horovits** 12:42 Oh, great, great! Yeah. Well, we're we're holding the fingers crossed that we get the slot there to to spread the word more formally over on the stage. But even if not, you know we can.
and knowing that you're there, which is amazing, then maybe we can touch base with with Dan and the team to see that we can get slots for the observatory. And let's see which other ways that we can leverage the The presence there.
**Adriel Perkins** 13:15 Yeah.
**Dotan Horovits** 13:16 Maybe even slots in the I think there's also like a project, regular project booths. I don't know how how it works and how they circulate that, or if once they have the observatory, it's less there relevant. But, like the regular project, booths also serve all sorts of, and maintainers in different capacities. So I need to see if I'm going to be there at Kubecon. But now that I know that you're going to be there, I'm I'm less under stress to to press for that.
**Adriel Perkins** 13:48 Appreciate it. Yeah. Looking forward to it, I've got 2 other talks submitted to and one's a tutorial so hopefully, hopefully, between 3 of the talks.
I'd hope all 3 get get accepted, but we'll see. That's not likely. So if we get accepted you'll see, and you'll find yourself very busy. Yes, for real.
**Dotan Horovits** 14:08 For real?
Well, yeah, yeah, maybe that's that's cool, anyway. Yeah, let's catch up once they publish the what what's up with with Kubecon and see how it goes.
Great. So I guess if if there's no other agenda items, we can give back the time to everyone. And wow!
**Adriel Perkins** 14:32 Sounds good.
**Dotan Horovits** 14:34 Cool. Y'all have a good day. Yeah.
**Martin Costello** 14:36 Bye, everyone.
**Dotan Horovits** 14:36 Hey? Everyone, bye-bye.
