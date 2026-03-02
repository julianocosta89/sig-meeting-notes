SIG: Agent Management WG
Date: 2025-08-06
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Andy Keller** 00:13 You might want to join and put your own video on, we can use this for audio. Yeah, we.
**Tigran Najaryan** 00:41 Because.
**Andy Keller** 00:41 Can you hear me?
**Evan Bradley** 00:48 Everyone.
**Andy Keller** 00:50 Hey!
**Tigran Najaryan** 00:52 I haven't.
Okay. I have the the 1st 2 lines there. Mostly just a call for reviews on the Prs.
The one that I listed particularly for 25. It's a bug fix actually.
Where the bug there, where we modify the shirt.
What is the Htp client, or whatever the default? Essentially, it's a shared global data structure.
We change it at the, you know, tests
the tests sometimes hit the bug essentially. So that fixes it.
Let's take a look at it. I need to merge it, first, st because it prevents some other
Prs from building as well the the bills.
Fail when that to be merged first, st
and we have a couple that are outstanding. If you have a moment, please take a look. We use some of those. I I saw the one that specifically asked you to take a look, and you confirm that it's working well for you. So I think we can measure that one which is good.
Okay? That's all I have.
the code I have. I think you have the the second 3rd item. There.
**dpaasman** 02:37 Yeah, yeah.
**Andy Keller** 02:37 Yeah, yeah, that next one. So I think the issue.
And then I do have pr open that addresses this issue.
But basically. So in this function loop that I link in the issue. This is our main function for reading from the web socket.
and then this for loop. Here, you know, we we read messages, and then we we respond to them with whatever our on message call back is giving us
The change here is
whenever we try to send the message over the Websocket connection, if we ever fail, is to break out of this loop.
that's the change, because right now we don't break out out of the loop. We just log in here, and then we continue on
We had a situation where we think the web socket was we were able to read from the websocket fine, but we just couldn't send it, and so we got stuck in this loop where we kept reading messages from the website connection. But we're never able to send a response and just
just stuck in that
loop and not didn't have a way to get out of it and fail to trigger the the clients reach back out and reconnect.
so this kind of
yeah. I I looked at it with Dakota. It was a strange situation. We're not. It's not easy to reproduce. We think I had to do with the particular proxy server. I was proxy the website for connection, and the
somehow they outbound would always fail.
Yeah.
**Tigran Najaryan** 04:22 You know, I think it makes total sense. If the sending fails.
something is wrong with the connection in an unknown way, I guess right, and it's likely that it will fail again, and we just the the safe approach here is, I agree to just disconnect it and let the client to reconnect.
So I think I agree with the change, if possible. I would like to see a test that verifies it, but that but if you can, somehow I don't know. Induce that condition, or just simulate a failure in some way.
And that the callback is also called.
Then I think it's fine. Yes, I agree with the change.
**Andy Keller** 05:07 Okay.
**Tigran Najaryan** 05:13 Okay.
**Andy Keller** 05:14 That was it for that.
**Tigran Najaryan** 05:15 That's all we have in the agenda. Michael, I think. Yes, I saw that Andy approved it.
We should. Let's I will merge the spec change.
then I think we should make a release from the spec repository, and then
use that version number in the in your go Pr.
**Michel Laterman** 05:35 Yep. Sounds good.
**Tigran Najaryan** 05:36 That work.
Okay.
**Michel Laterman** 05:38 Yeah, it? Works.
**Tigran Najaryan** 05:40 Okay, let's do that.
I think you have another one. You had 2 right. You had 2 open.
**Michel Laterman** 05:46 The other one is for proxy changes. And last week
I ended up making my own library to provide a dialer that can set the connection headers.
Yeah, that was, you can use that with
the Websockets library, because it doesn't look like it's actively maintained right. Now.
**Tigran Najaryan** 06:12 Yeah.
okay. I saw you replied to to my comments there, I didn't see. I just saw your reply, so I will take a look.
**Michel Laterman** 06:20 Yeah, I guess the question that I guess can be raised to the group is
as part of the proxy support changes. I've made a change, so that clients by default
will scan for proxy environment variables.
Is that a change?
We should keep.
**Tigran Najaryan** 06:42 Isn't that the default behavior for.
**Michel Laterman** 06:45 I'll just.
**Tigran Najaryan** 06:45 Vp, client.
**Michel Laterman** 06:47 The Http client. Yes, for the Web sockets, client. I don't think so.
**Tigran Najaryan** 06:53 Okay?
And that would be using the same environment. Variable.
**Michel Laterman** 06:59 Yeah. The http.
**Tigran Najaryan** 07:01 Right.
**Michel Laterman** 07:01 Http. Proxy, Https proxy, and no proxy that were used by most programs.
**Tigran Najaryan** 07:11 Yeah, I think it makes sense to me. I don't know what
would be wrong with that approach. Yes, it's a change in behavior.
but perhaps sort of expected that it should be working like that.
**Michel Laterman** 07:30 Okay.
**Tigran Najaryan** 07:35 I don't know if others have a different opinion here, but it seems like or reasonable.
reasonable approach. I would expect that. Yes, if Http. Underscore proxy variable is honored by the Http. Transport
should be also honored by the Websocket transport the same way.
It's just consistent.
Yeah.
Okay.
Good.
**Andy Keller** 08:09 Egreg. Do you want to go through these prs and assign them?
and I cause I know that some some of them you're in discussion with some people on, and some of them
sort of repo housekeeping, if you will.
**Tigran Najaryan** 08:28 You want to do what assign the Prs.
**Andy Keller** 08:32 Yeah, just I just wanna I just wanna make sure I'm reviewing what what we need to review. And some of these seem like they're
**Tigran Najaryan** 08:41 Sure. I mean we can. I don't know Round Robin, or something like that between the approvers.
**Andy Keller** 08:48 Well, I I guess I'm just. I don't know which of these are. Are ready to go.
It looks like this, this 3. If we start at the bottom is 3 80
was reopened last week.
There's a merge conflict, probably rather recent.
**Tigran Najaryan** 09:13 Yeah.
**Andy Keller** 09:14 And it looks like you and and Michael, boast.
Discuss this.
**Tigran Najaryan** 09:22 Yeah.
okay, so you, you want to know which ones essentially require your attention. That's what I'm hearing.
**Andy Keller** 09:35 Yes, that'd be that'd be helpful. I'm.
**Tigran Najaryan** 09:37 Yeah.
**Andy Keller** 09:37 Look at all of them. But if if if in particular, you'd like to, just.
**Tigran Najaryan** 09:42 Yeah, yeah.
Well, yeah, I can do it just like I did for the other pr, from Michael, where I wanted your input, I can go over the ones that I already reviewed
and where I'm maybe waiting for additional input from your anybody else. I can tag you guys if that works.
I don't know if you want some other approach, whatever we can.
**Andy Keller** 10:08 Been.
I look at this list often, and it's
you know, and I and it's growing and a lot of them are old, and I'd I'd like to.
you know, either merge or close some of these and but but they're.
**Tigran Najaryan** 10:23 I'm I'm with you. Yeah, yeah. Whatever you think would work better. I I agree. Let's
make faster progress on the Prs right? Measure them quicker or or close them quicker if we don't like them.
If you can think of a a good process here.
I'm here. I don't know. I'm open to the ideas. What would you like to do
anybody here? If you've got some suggestions?
We don't have the automation that we have more in the other repositories like, I know, Evan, we have
a ton of helpers in the Collector Repository which helped keep
maintainers attention focused on the Prs and closing on making sure. If they they, if they go stale, they're close, and all that stuff. We're probably not there yet. We don't have that volume of work to do here in the suppository. We could at some point borrow some of the tooling that you have.
I don't know. We we could try that as well.
or maybe we go with some some manual process process, for now, initially.
**Andy Keller** 11:29 Yeah, well, I just, I just wanna
yeah. I guess I just wanna make sure I'm on staying on top of it. But also
it seems like a lot of these are in flight.
And yeah, I did approve your.
**Tigran Najaryan** 11:49 So here.
**Andy Keller** 11:50 You're fixed, and I'm happy to merge that.
**Tigran Najaryan** 11:53 Yeah. So I don't know. My, my initial suggestion here would be that
we probably ping each other when we want other input.
And if we're not, we would just imagine, go ahead right? Something like that which is just normally what I do, but maybe not very systematically, not always. Maybe I could try to be a bit more consistent there, and you guys could do the same right if you took a look. You're happy with that. But you still would like a second opinion.
Also you can tag somebody else.
**Andy Keller** 12:28 Yeah. Michael sent me up on the Cnc. Of slack a couple of times, and that's helpful, too.
**Tigran Najaryan** 12:32 Yes, yes. Yeah.
Okay. Let's maybe let's try that. And if that doesn't work well, we will look into a bit more. I don't know automation or something like that.
**Andy Keller** 12:44 Yeah. Okay.
Sounds, good.
**Evan Bradley** 12:46 So I do want to say, feel free to ping me. If you guys ever want a second look, or you just want me to take a look at something. Usually I see in my notifications that somebody else has already taken a look, and so I'll just go off to some other. Pr. But if if you're short on time or something, let me know.
**Tigran Najaryan** 13:04 Okay. Sounds. Good.
Okay. Anything. Else. Anyone.
**Andy Keller** 13:15 Nope.
**Tigran Najaryan** 13:19 Good. Thank you.
**Andy Keller** 13:21 All right.
**Tigran Najaryan** 13:22 Bye.
**Andy Keller** 13:22 If we expect that.
